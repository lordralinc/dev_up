import abc
import typing as ty


class SessionABC(abc.ABC):

    @abc.abstractmethod
    async def close(self) -> ty.NoReturn:
        ...

    @abc.abstractmethod
    async def make_post_request(self, url: str, data: ty.Optional[ty.Dict[str, ty.Any]]) -> ty.Any:
        ...

    @abc.abstractmethod
    async def make_json(self, url: str, data: ty.Optional[ty.Dict[str, ty.Any]]) -> ty.Union[ty.Dict, ty.List]:
        ...
