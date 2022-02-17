import typing as ty

from dev_up.base.models import ResponseModel


class VKUserGetSubscriptionsResponse(ResponseModel):
    user_id: int
    count: int
    subscriptions: ty.List[int]
