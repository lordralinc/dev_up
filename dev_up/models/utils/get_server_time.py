from pydantic import BaseModel
from datetime import datetime as dt

__all__ = (
    'UtilsGetServerTimeResponse',
    'UtilsGetServerTime',
)


class UtilsGetServerTimeResponse(BaseModel):
    date: int

    @property
    def datetime(self) -> dt:
        return dt.fromtimestamp(self.date / 1000)


class UtilsGetServerTime(BaseModel):
    response: UtilsGetServerTimeResponse
