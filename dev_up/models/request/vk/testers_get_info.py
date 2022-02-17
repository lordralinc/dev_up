from dev_up.base.models import RequestModel

__all__ = (
    'VKTestersGetInfoRequest',
)


class VKTestersGetInfoRequest(RequestModel):
    user_id: int
