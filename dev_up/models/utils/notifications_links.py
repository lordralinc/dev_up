from pydantic import BaseModel


class UtilsNotificationsLinksResponse(BaseModel):
    notifications: bool


class UtilsNotificationsLinks(BaseModel):
    response: UtilsNotificationsLinksResponse
