from datetime import datetime

from pydantic import BaseModel


class UtilsCheckLinkResponse(BaseModel):
    url: str
    original_url: str


class UtilsCheckLink(BaseModel):
    response: UtilsCheckLinkResponse
