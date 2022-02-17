import typing as ty
import urllib.parse

import cachetools
import loguru

from dev_up.abc.json import JsonParserABC
from dev_up.abc.session import SessionABC
from dev_up.base.json import JsonParser
from dev_up.base.models import RequestModel, REQUEST_MODEL, RESPONSE_MODEL
from dev_up.base.session import AiohttpSession
from dev_up.categories.api import APICategories
from dev_up.exceptions import DevUpResponseException

URL_GENERATOR = ty.Callable[["DevUpAPI", str], str]


class DevUpAPI(APICategories):
    base_url: str = "dev-up.ru"

    def __init__(
            self,
            access_token: ty.Optional[str] = None,
            session: ty.Optional[SessionABC] = None,
            json_parser: ty.Optional[JsonParserABC] = None,
            base_url: str = "dev-up.ru",
            raise_error: ty.Optional[bool] = True,
            raw_response: ty.Optional[bool] = False,
            cache_table: ty.Optional[cachetools.Cache] = None,
            use_cache: bool = False
    ):
        self.base_url = base_url

        self._access_token = access_token
        self._json_parser = json_parser or JsonParser()
        self._session = session or AiohttpSession(json_parser=self._json_parser)

        self._raise_error = raise_error
        self._raw_response = raw_response
        self._cache_table = cache_table or cachetools.TTLCache(
            ttl=7200, maxsize=2 ** 12
        )
        self._use_cache = use_cache

    def get_instance(self) -> "DevUpAPI":
        return self

    def default_url_generator(self, method: str) -> str:
        return "https://api.{base_url}/method/{method}".format(
            base_url=self.base_url,
            method=method
        )

    async def close(self) -> ty.NoReturn:
        await self._session.close()

    async def __aenter__(self) -> "DevUpAPI":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def clear_cache(self):
        self._cache_table.clear()

    @staticmethod
    async def _validate_request(
            data: ty.Dict[str, ty.Any],
            kwargs: ty.Dict[str, ty.Any] = None,
            access_token: ty.Optional[str] = None,
            request_model: ty.Type[REQUEST_MODEL] = dict
    ) -> REQUEST_MODEL:
        loguru.logger.debug(f"Validate request data {data!r}")
        if isinstance(data, RequestModel):
            data = data.dict()
        data.update(key=access_token, **kwargs)
        return request_model(**data)

    @staticmethod
    async def _prepare_request(data: ty.Dict[str, ty.Any]) -> ty.Dict[str, ty.Any]:
        return {k: v for k, v in data.items() if v is not None}

    async def _validate_response(
            self,
            url: str,
            data: dict,
            raw_response: bool = None,
            raise_error: bool = None,
            response_model: ty.Type[RESPONSE_MODEL] = dict
    ) -> RESPONSE_MODEL:
        loguru.logger.debug(f"Validate response data {data!r}")
        raw_response = raw_response if raw_response is not None else self._raw_response
        raise_error = raise_error if raise_error is not None else self._raise_error

        if raw_response:
            return data
        if 'err' in data and raise_error:
            raise DevUpResponseException(
                url, **data['err']
            )
        elif 'error' in data:
            return data
        else:
            return response_model(**data['response'] if isinstance(data['response'], dict) else data['response'])

    @staticmethod
    def _get_cache_path(url: str, data: ty.Union[ty.Dict[str, ty.Any], RequestModel]) -> str:
        cache_hash = urllib.parse.urlencode(data if isinstance(data, dict) else data.dict())
        return "{url}#{cache_hash}".format(url=url, cache_hash=cache_hash)

    async def make_request(
            self,
            method: str,
            data: ty.Union[ty.Dict[str, ty.Any], RequestModel, None] = None,
            access_token: ty.Optional[str] = None,
            request_model: ty.Type[REQUEST_MODEL] = dict,
            response_model: ty.Type[RESPONSE_MODEL] = dict,
            url_generator: URL_GENERATOR = default_url_generator,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None,
            **kwargs
    ) -> RESPONSE_MODEL:
        use_cache = use_cache if use_cache is not None else self._use_cache
        cache_path = None

        url = url_generator(self, method)

        loguru.logger.debug(f"Make request to {url} with data {data!r}")
        data_to_request = await self._validate_request(
            data or {},
            kwargs or {},
            access_token or self._access_token,
            request_model
        )

        if use_cache or (use_cache is None and self._use_cache):
            cache_path = self._get_cache_path(url, data_to_request)
            if cache_path in self._cache_table:
                loguru.logger.debug(f"Get response from cache: {self._cache_table[cache_path]!r}")
                return await self._validate_response(
                    url,
                    self._cache_table[cache_path],
                    raw_response,
                    raise_error,
                    response_model
                )

        response = await self._session.make_json(
            url,
            await self._prepare_request(
                dict(data_to_request) if not isinstance(data_to_request, RequestModel) else data_to_request.dict()
            )
        )
        if use_cache or (use_cache is None and self._use_cache):
            self._cache_table[cache_path] = response
        return await self._validate_response(url, response, raw_response, raise_error, response_model)
