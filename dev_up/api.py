from typing import Union, Type, TypeVar

import requests
import asyncio
import aiohttp
from pydantic import BaseModel, ValidationError
from attrdict import AttrDict

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

    @property
    def api_instance(self) -> "DevUpAPI":
        return self

    def __init__(
            self,
            token: str,
            loop: asyncio.AbstractEventLoop = None,
            pass_return_response: bool = False,
            timeout: float = 30,
    ):
        self.pass_return_response = pass_return_response
        self._token = token
        self._loop = loop

        self.timeout = timeout

    def make_request(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        """Выполняет запрос к серверу DEV-UP

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        if data is None:
            data = dict()
        data.update(key=self._token)
        logger.debug(
            f"Make post request to https://api.dev-up.ru/method/{method} with data {data}. Timeout {self.timeout}"
        )
        response = requests.post(f"https://api.dev-up.ru/method/{method}", data=data, timeout=self.timeout).json()
        logger.debug(f"Response: {response}. Use dataclass {dataclass.__name__}.")

        if 'err' in response:
            raise DevUpException(**response['err'])
        try:
            data = dataclass(**response)
            logger.debug("Response validated")
            return data
        except ValidationError as ex:
            logger.exception(ex)
            return AttrDict(response)

    async def make_request_async(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        """Выполняет запрос к серверу DEV-UP (асинхронно)

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        if data is None:
            data = dict()
        data.update(key=self._token)
        logger.debug(
            f"Make async post request to https://api.dev-up.ru/method/{method} with data {data}. Timeout {self.timeout}"
        )
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with session.post(f"https://api.dev-up.ru/method/{method}", data=data) as response:
                response_json = await response.json()
                logger.debug(f"Response: {response_json}. Use dataclass {dataclass.__name__}.")
                if 'err' in response_json:
                    raise DevUpException(**response_json['err'])
                try:
                    data = dataclass(**response_json)
                    logger.debug("Response validated")
                    return data
                except ValidationError as ex:
                    logger.exception(ex)
                    return AttrDict(response_json)

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop
