from dev_up.base.models import RequestModel

__all__ = (
    'VKGetStickersRequest',
)


class VKGetStickersRequest(RequestModel):
    user_id: int
