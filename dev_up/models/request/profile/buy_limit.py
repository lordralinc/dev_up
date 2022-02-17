from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'ProfileBuyLimitRequest',
)


class ProfileBuyLimitRequest(RequestModel):
    amount: int = Field(title="Количество")
