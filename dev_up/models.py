from typing import List

from pydantic import BaseModel


class Description(BaseModel):
    ru: str
    en: str
    kz: str
    uk: str


#
# vk.getStickers
#

class Stickers(BaseModel):
    count: int
    packs_name: List[str]


class GetStickers(BaseModel):
    user_id: int
    stickers: Stickers


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
    groups: List[Group]
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
    apps: List[App]
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


class ProfileGet(BaseModel):
    id: int
    id_vk: int
    first_name: str
    last_name: str
    verified: int
    api: ProfileGetApi


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
