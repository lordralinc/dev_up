import typing

import pydantic
from pydantic import Field

from dev_up.abc.models import RequestABC, ResponseABC


class RequestModel(pydantic.BaseModel, RequestABC):
    key: str = Field(
        title="Ключ доступа VK",
        repr=False
    )

    def __repr_args__(self: pydantic.BaseModel):
        return [
            (key, value)
            for key, value in self.__dict__.items()
            if self.__fields__[key].field_info.extra.get("repr", True)
        ]

    def __getitem__(self, y):
        return self.__getattribute__(y)


class ResponseModel(pydantic.BaseModel, ResponseABC):

    def __getitem__(self, y):
        return self.__getattribute__(y)


REQUEST_MODEL = typing.TypeVar('REQUEST_MODEL', RequestModel, dict)
RESPONSE_MODEL = typing.TypeVar('RESPONSE_MODEL', ResponseModel, dict)
