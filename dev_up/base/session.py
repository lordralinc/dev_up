import typing as ty

import aiohttp

from dev_up.abc.json import JsonParserABC
from dev_up.abc.session import SessionABC
from dev_up.base.json import JsonParser


class AiohttpSession(SessionABC):

    def __init__(
            self,
            json_parser: ty.Optional[JsonParserABC] = None,
            session: ty.Optional[aiohttp.ClientSession] = None,
            **session_kwargs
    ):
        self._json_parser = json_parser or JsonParser()
        self._session = session
        self._session_kwargs = session_kwargs

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session and self._session.closed:
            self._session = aiohttp.ClientSession(
                json_serialize=self._json_parser.dumps,
                raise_for_status=True,
                **self._session_kwargs
            )
        elif not self._session:
            self._session = aiohttp.ClientSession(
                json_serialize=self._json_parser.dumps,
                raise_for_status=True,
                **self._session_kwargs
            )
        return self._session

    async def close(self) -> ty.NoReturn:
        await self.session.close()
        self._session = None

    async def make_post_request(self, url: str, data: ty.Optional[ty.Dict[str, ty.Any]]) -> ty.Any:
        async with self.session.post(url, data=data) as response:
            return await response.read()

    async def make_json(self, url: str, data: ty.Optional[ty.Dict[str, ty.Any]]) -> ty.Union[ty.Dict, ty.List]:
        return self._json_parser.loads(await self.make_post_request(url, data))
