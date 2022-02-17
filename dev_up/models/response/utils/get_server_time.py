from datetime import datetime as dt

from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'UtilsGetServerTimeResponse',
)


class UtilsGetServerTimeResponse(ResponseModel):
    date: int = Field(title="Дата и время в формате timestamp")

    @property
    def datetime(self) -> dt:
        return dt.fromtimestamp(self.date / 1000)
