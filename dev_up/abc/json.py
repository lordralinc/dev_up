import abc
import typing as ty


class JsonParserABC(abc.ABC):

    @abc.abstractmethod
    def dumps(self, data: ty.Dict[str, ty.Any]) -> str:
        ...

    @abc.abstractmethod
    def loads(self, data: ty.Union[str, bytes]) -> ty.Dict[str, ty.Any]:
        ...
