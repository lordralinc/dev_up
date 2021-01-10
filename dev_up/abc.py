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
