from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'ProfileGetBalanceLinkRequest',
)


class ProfileGetBalanceLinkRequest(RequestModel):
    amount: int = Field(title="Количество")
    vk: int = Field(title="VK ID")
