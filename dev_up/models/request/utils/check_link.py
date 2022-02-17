from pydantic import Field, AnyUrl

from dev_up.base.models import RequestModel

__all__ = (
    'UtilsCheckLinkRequest',
)


class UtilsCheckLinkRequest(RequestModel):
    url: AnyUrl = Field(title="Ссылка")
