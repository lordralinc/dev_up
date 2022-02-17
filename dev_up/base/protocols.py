import abc
import typing as ty


class SupportsPettyPrint(ty.Protocol):

    @abc.abstractmethod
    def __petty_print__(self) -> str:
        raise NotImplemented
