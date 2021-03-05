from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProfileGetResponseApi(BaseModel):
    key: str
    balance: float
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
    last_ip: Optional[str]
    last_online: int
    req_time: int
    api: Optional[ProfileGetResponseApi]

    @property
    def last_online_datetime(self):
        return datetime.fromtimestamp(self.last_online / 1000)

    @property
    def req_datetime(self):
        return datetime.fromtimestamp(self.req_time / 1000)


class ProfileGet(BaseModel):
    response: ProfileGetResponse
