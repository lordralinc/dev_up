from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'UtilsGetWebInfoRequest',
)


class UtilsGetWebInfoRequest(RequestModel):
    address: str = Field(title="IP адрес или ссылка")
