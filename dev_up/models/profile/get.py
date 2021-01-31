from datetime import datetime

from pydantic import BaseModel

__all__ = (
    'ProfileGetResponseApi',
    'ProfileGetResponse',
    'ProfileGet',
)


class ProfileGetResponseApi(BaseModel):
    key: str
    limit: int
    rate_limit: int
    warn: int
    used: int


class ProfileGetResponse(BaseModel):
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
    api: ProfileGetResponseApi

    @property
    def last_online_datetime(self):
        return datetime.fromtimestamp(self.last_online / 1000)

    @property
    def req_datetime(self):
        return datetime.fromtimestamp(self.req_time / 1000)


class ProfileGet(BaseModel):
    response: ProfileGetResponse
