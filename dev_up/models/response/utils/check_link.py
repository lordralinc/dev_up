from pydantic import Field, AnyUrl

from dev_up.base.models import ResponseModel

__all__ = (
    'UtilsCheckLinkResponse',
)


class UtilsCheckLinkResponse(ResponseModel):
    url: AnyUrl = Field(title="Сокращенная ссылка")
    original_url: AnyUrl = Field(title="Оригинальная ссылка")
