from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'ProfileBuyPremiumResponse',
)


class ProfileBuyPremiumResponse(ResponseModel):
    success: bool = Field(title="Успешен ли запрос")
