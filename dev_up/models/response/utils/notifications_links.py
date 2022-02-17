from dev_up.base.models import ResponseModel

__all__ = (
    'UtilsNotificationsLinksResponse',
)


class UtilsNotificationsLinksResponse(ResponseModel):
    notifications: bool
