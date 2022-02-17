from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'ProfileBuyLimitResponse',
)


class ProfileBuyLimitResponse(ResponseModel):
    success: bool = Field(title="Успешен ли запрос")
