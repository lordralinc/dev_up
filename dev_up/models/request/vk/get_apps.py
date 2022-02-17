from dev_up.base.models import RequestModel

__all__ = (
    'VKGetAppsRequest',
)


class VKGetAppsRequest(RequestModel):
    user_id: int
