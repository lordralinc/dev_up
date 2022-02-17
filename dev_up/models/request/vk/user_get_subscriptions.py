from dev_up.base.models import RequestModel

__all__ = (
    'VKUserGetSubscriptionsRequest',
)


class VKUserGetSubscriptionsRequest(RequestModel):
    user_id: int
