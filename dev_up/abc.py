import asyncio
import typing as ty
from attrdict import AttrDict
from pydantic import BaseModel
from abc import ABC, abstractmethod

T = ty.TypeVar('T', dict, AttrDict, BaseModel)


class DevUpAPIABC(ABC):

    @property
    @abstractmethod
    def api_instance(self) -> "DevUpAPIABC":
        ...

    @abstractmethod
    def make_request(
            self,
            method: str,
            data: dict = None,
            dataclass: ty.Type[T] = AttrDict,
            url: ty.Callable[[str, str], str] = lambda a, b: a
    ) -> T:
        ...

    @abstractmethod
    async def make_request_async(
            self,
            method: str,
            data: dict = None,
            dataclass: ty.Type[T] = AttrDict,
            url: ty.Callable[[str, str], str] = lambda a, b: a
    ) -> T:
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
    def audio(self) -> "BaseAPICategoriesABC":
        ...

    @property
    @abstractmethod
    def profile(self) -> "BaseAPICategoriesABC":
        ...

    @property
    @abstractmethod
    def utils(self) -> "BaseAPICategoriesABC":
        ...
    
    @property
    @abstractmethod
    def vk(self) -> "BaseAPICategoriesABC":
        ...

    @property
    @abstractmethod
    def warface(self) -> "BaseAPICategoriesABC":
        ...