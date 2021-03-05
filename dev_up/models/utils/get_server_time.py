from datetime import datetime as dt

from pydantic import BaseModel


class UtilsGetServerTimeResponse(BaseModel):
    date: int

    @property
    def datetime(self) -> dt:
        return dt.fromtimestamp(self.date / 1000)


class UtilsGetServerTime(BaseModel):
    response: UtilsGetServerTimeResponse
