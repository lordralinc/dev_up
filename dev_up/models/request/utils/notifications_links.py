import enum

from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'UtilsNotificationsLinksStatus',
    'UtilsNotificationsLinksRequest',
)


class UtilsNotificationsLinksStatus(enum.IntEnum):
    ON = 2
    OFF = 1


class UtilsNotificationsLinksRequest(RequestModel):
    code: str = Field(title="Код ссылки")
    status: UtilsNotificationsLinksStatus = Field(title="Статус")
