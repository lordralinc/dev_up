import requests
import asyncio
import aiohttp

from dev_up.abc import DevUpAPIABC
from dev_up.categories import APICategories
from dev_up.exceptions import DevUpException

import logging

logger = logging.getLogger(__name__)


class DevUpAPI(DevUpAPIABC, APICategories):

    @property
    def api_instance(self) -> "DevUpAPI":
        return self

    def __init__(
            self,
            token: str,
            loop: asyncio.AbstractEventLoop = None
    ):
        self._token = token
        self._loop = loop

    def make_request(self, method: str, data=None) -> dict:
        if data is None:
            data = dict()
        data.update(key=self._token)
        logger.debug(f"Make post request to https://api.dev-up.ru/method/{method} with data {data}")
        response = requests.post(f"https://api.dev-up.ru/method/{method}", data=data).json()
        logger.debug(f"Response: {response}")

        if 'err' in response:
            raise DevUpException(
                params=response['params'],
                **response['err']
            )

        return response

    async def make_request_async(self, method: str, data=None) -> dict:
        if data is None:
            data = dict()
        data.update(key=self._token)
        logger.debug(f"Make async post request to https://api.dev-up.ru/method/{method} with data {data}")
        async with aiohttp.ClientSession() as session:
            async with session.post(f"https://api.dev-up.ru/method/{method}", data=data) as response:
                response_json = await response.json()
                logger.debug(f"Response: {response_json}")
                if 'err' in response_json:
                    raise DevUpException(
                        params=response_json['params'],
                        **response_json['err']
                    )
                return response_json

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop
