from pydantic import Field, AnyUrl

from dev_up.base.models import ResponseModel

__all__ = (
    'ProfileGetBalanceLinkResponse',
)


class ProfileGetBalanceLinkResponse(ResponseModel):
    url: AnyUrl = Field(title="Ссылка на пополнение баланса")
