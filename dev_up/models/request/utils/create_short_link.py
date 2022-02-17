from pydantic import AnyUrl, Field

from dev_up.base.models import RequestModel

__all__ = (
    'UtilsCreateShortLinkRequest',
)


class UtilsCreateShortLinkRequest(RequestModel):
    url: AnyUrl = Field(title="Ссылка")
