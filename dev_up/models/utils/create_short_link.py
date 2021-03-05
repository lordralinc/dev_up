from datetime import datetime

from pydantic import BaseModel


class ShortLink(BaseModel):
    url: str
    code: str


class UtilsCreateShortLinkResponse(BaseModel):
    id: int
    create_vk: int
    original_url: str
    create_date: int
    notifications: bool
    link: ShortLink

    @property
    def create_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.create_date / 1000)


class UtilsCreateShortLink(BaseModel):
    response: UtilsCreateShortLinkResponse
