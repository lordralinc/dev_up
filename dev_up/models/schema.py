import typing as ty

from pydantic import BaseModel


class GetAppsSchema(BaseModel):
    method: str
    request_model: ty.Type[BaseModel]
    response_model: ty.Type[BaseModel]
