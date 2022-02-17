from datetime import datetime as dt

from pydantic import Field, BaseModel

from dev_up.base.models import ResponseModel

__all__ = (
    'UtilsCreateShortLinkShortLink',
    'UtilsCreateShortLinkResponse',
)


class UtilsCreateShortLinkShortLink(BaseModel):
    url: str = Field(title="")
    code: str = Field(title="")


class UtilsCreateShortLinkResponse(ResponseModel):
    id: int = Field(title="")
    create_vk: int = Field(title="")
    original_url: str = Field(title="")
    create_date: int = Field(title="")
    notifications: bool = Field(title="")
    link: UtilsCreateShortLinkShortLink = Field(title="")

    @property
    def create_datetime(self) -> dt:
        return dt.fromtimestamp(self.create_date / 1000)
