from datetime import datetime
from enum import IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel


class Description(BaseModel):
    ru: str
    en: str
    kz: str
    uk: str


#
# vk.getStickers
#

class StickersPrice(BaseModel):
    votes: int
    rub: int


class Sticker(BaseModel):
    id: int
    pack_id: int
    name: str
    stickers_count: Optional[int] = None
    author: Optional[str] = None
    description: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[StickersPrice] = None
    url_buy: Optional[str] = None


class GetStickers(BaseModel):
    user_id: int
    count: int
    stickers: List[Sticker]
    price: Optional[StickersPrice] = None


class VkGetStickersResponse(BaseModel):
    response: GetStickers


#
# vk.getGroups
#

class Group(BaseModel):
    id: int
    name: str
    photo: str
    domain: str
    members_count: int
    verified: int


class GetGroups(BaseModel):
    user_id: int
    count: int
    groups: Optional[List[Group]]
    description: Description


class VkGetGroupsResponse(BaseModel):
    response: GetGroups


#
# vk.getApps
#

class App(BaseModel):
    id: int
    name: str
    photo: str
    domain: str
    members_count: int


class GetApps(BaseModel):
    user_id: int
    count: int
    apps: Optional[List[App]]
    description: Description


class VkGetAppsResponse(BaseModel):
    response: GetApps


#
# profile.get
#

class ProfileGetApi(BaseModel):
    key: str
    limit: int
    rate_limit: int
    warn: int


class ProfileGet(BaseModel):
    id: int
    id_vk: int
    first_name: str
    last_name: str
    verified: int
    premium: bool
    notifications: bool
    last_ip: str
    last_online: int
    req_time: int
    api: ProfileGetApi

    @property
    def last_online_datetime(self):
        return datetime.fromtimestamp(self.last_online)

    @property
    def req_datetime(self):
        return datetime.fromtimestamp(self.req_time)


class ProfileGetResponse(BaseModel):
    response: ProfileGet


#
# audio.speech
#

class SpeechResponse(BaseModel):
    url: str
    text: str


class AudioSpeechResponse(BaseModel):
    response: SpeechResponse


#
# utils.md5Generate
#

class MD5GenerateResponse(BaseModel):
    date: str


class UtilsMD5GenerateResponse(BaseModel):
    response: MD5GenerateResponse


#
# utils.getServerTime
#
class GetServerTimeResponse(BaseModel):
    date: int


class UtilsGetServerTimeResponse(BaseModel):
    response: GetServerTimeResponse


#
# utils.getShortLink
#

class ShortLink(BaseModel):
    url: str
    code: str


class GetShortLinkResponse(BaseModel):
    id: int
    create_vk: int
    original_url: str
    create_date: int
    notifications: bool
    link: ShortLink

    @property
    def create_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.create_date)


class UtilsGetShortLinkResponse(BaseModel):
    response: GetShortLinkResponse


#
# utils.notificationsLinks
#

class UtilsNotificationsLinks(BaseModel):
    notifications: bool


class UtilsNotificationsLinksResponse(BaseModel):
    response: UtilsNotificationsLinks


class LinkStatus(IntEnum):
    ON = 2
    OFF = 1
