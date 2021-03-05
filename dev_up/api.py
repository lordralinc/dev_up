import asyncio
from typing import Type, TypeVar, Dict

import aiohttp
import requests
from attrdict import AttrDict
from pydantic import BaseModel, ValidationError

from dev_up import const
from dev_up.abc import DevUpAPIABC
from dev_up.categories import APICategories
from dev_up.exceptions import DevUpException

try:
    from loguru import logger
except ImportError:
    import logging

    logger = logging.getLogger(__name__)

T = TypeVar('T', dict, AttrDict, BaseModel)


class DevUpAPI(DevUpAPIABC, APICategories):

    URL = "https://api.dev-up.ru/method/{method}"

    @property
    def api_instance(self) -> "DevUpAPI":
        return self

    def __init__(
            self,
            token: str = None,
            loop: asyncio.AbstractEventLoop = None,
            raise_validation_error: bool = False,
            return_response: bool = False,
            timeout: float = 30,
    ):
        self.return_response = return_response
        self._token = token
        self._loop = loop
        self.raise_validation_error = raise_validation_error
        self.timeout = timeout

    def __repr__(self) -> str:
        return (
            f"<DevUpAPI("
            f"return_response={self.return_response}, "
            f"raise_validation_error={self.raise_validation_error}, "
            f"timeout={self.timeout}, "
            f"token={'static' if self._token else 'dynamic'}"
            f")>"
        )

    def make_request(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        """Выполняет запрос к серверу DEV-UP

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        if data is None:
            data = dict()
        data['key'] = data.get('key', None) or self._token

        request_url = self.URL.format(method=method)
        logger.debug(
            f"Make post request to {request_url} with data {self.data_to_print(data)}. Timeout {self.timeout}"
        )
        response = requests.post(request_url, data=data, timeout=self.timeout)
        response.raise_for_status()
        response_json = response.json()
        logger.debug(f"Response: {response_json}. Use dataclass {dataclass.__name__}.")
        return self.validate_response(response_json, dataclass)

    async def make_request_async(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        """Выполняет запрос к серверу DEV-UP (асинхронно)

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        if data is None:
            data = dict()
        data['key'] = data.get('key', None) or self._token

        request_url = self.URL.format(method=method)
        logger.debug(
            f"Make async post request to {request_url} with data {self.data_to_print(data)}. Timeout {self.timeout}"
        )
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with session.post(request_url, data=data) as response:
                response.raise_for_status()
                response_json = await response.json()
                logger.debug(f"Response: {response_json}.")
                return self.validate_response(response_json, dataclass)


    def validate_response(self, response: Dict, dataclass: Type[T]) -> T:
        if 'err' in response:
            raise DevUpException(**response['err'])
        try:
            data = dataclass(**response)
            logger.debug(f"Response validated with dataclass {dataclass.__name__}")
            return data
        except ValidationError as ex:
            if self.raise_validation_error:
                raise ex
            logger.error(f"Response validated with dataclass AttrDict")
            return AttrDict(response)

    @staticmethod
    def data_to_print(data: Dict) -> Dict:
        new_dict = {}
        for k, v in data.items():
            if k == 'key':
                new_dict[k] = v[:4] + '*' * 4 + v[-4:]
            else:
                new_dict[k] = v
        return new_dict

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop

    @loop.setter
    def loop(self, new_loop: asyncio.AbstractEventLoop):
        self._loop = new_loop

    @property
    def author(self) -> str:
        return const.__author__

    @property
    def version(self) -> str:
        return const.__version__
