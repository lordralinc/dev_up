import abc
import typing as ty


class DevUpAPIABC(abc.ABC):

    @abc.abstractmethod
    async def close(self) -> ty.NoReturn:
        ...

    def get_instance(self) -> "DevUpAPIABC":
        ...

    async def make_request(
            self,
            *args,
            **kwargs
    ) -> ty.Any:
        ...
