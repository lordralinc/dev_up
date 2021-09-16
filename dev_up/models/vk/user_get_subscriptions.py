import typing as ty

from pydantic import BaseModel


class VkUserGetSubscriptionsResponse(BaseModel):
    user_id: int
    count: int
    subscriptions: ty.List[int]


class VkUserGetSubscriptions(BaseModel):
    response: VkUserGetSubscriptionsResponse