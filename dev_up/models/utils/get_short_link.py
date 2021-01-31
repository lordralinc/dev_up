from datetime import datetime

from pydantic import BaseModel

__all__ = (
    'ShortLink',
    'UtilsGetShortLinkResponse',
    'UtilsGetShortLink',
)


class ShortLink(BaseModel):
    url: str
    code: str


class UtilsGetShortLinkResponse(BaseModel):
    id: int
    create_vk: int
    original_url: str
    create_date: int
    notifications: bool
    link: ShortLink

    @property
    def create_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.create_date / 1000)


class UtilsGetShortLink(BaseModel):
    response: UtilsGetShortLinkResponse
