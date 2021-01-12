import asyncio
from abc import ABC, abstractmethod


class DevUpAPIABC(ABC):

    @property
    @abstractmethod
    def api_instance(self) -> "DevUpAPIABC":
        ...

    @abstractmethod
    def make_request(
            self,
            method: str,
            data=None
    ) -> dict:
        ...

    @abstractmethod
    async def make_request_async(
            self,
            method: str,
            data=None
    ) -> dict:
        ...

    @property
    @abstractmethod
    def loop(self) -> asyncio.AbstractEventLoop:
        ...


class BaseAPICategoriesABC(ABC):
    ...


class APICategoriesABC(ABC):

    @property
    @abstractmethod
    def vk(self) -> "BaseAPICategoriesABC":
        ...

    @property
    @abstractmethod
    def profile(self) -> "BaseAPICategoriesABC":
        ...

    @property
    @abstractmethod
    def audio(self) -> "BaseAPICategoriesABC":
        ...
