from pydantic import BaseModel

__all__ = (
    'UtilsNotificationsLinksResponse',
    'UtilsNotificationsLinks',
)


class UtilsNotificationsLinksResponse(BaseModel):
    notifications: bool


class UtilsNotificationsLinks(BaseModel):
    response: UtilsNotificationsLinksResponse
