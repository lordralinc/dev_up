from dev_up.base.models import RequestModel

__all__ = (
    'VKGetGroupsRequest',
)


class VKGetGroupsRequest(RequestModel):
    user_id: int
