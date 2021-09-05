from datetime import datetime, timedelta
from typing import Optional, Union

from pydantic import BaseModel


class ProfileGetResponseApi(BaseModel):
    key: str
    balance: float
    limit: int
    rate_limit: int
    warn: int
    used: int


class ProfileGetResponseLP(BaseModel):
    created: bool
    status: bool


class ProfileGetResponse(BaseModel):
    id: int
    id_vk: int
    first_name: str
    last_name: str
    verified: int
    premium: Union[int, bool]
    unlimited: bool
    ban: bool
    banip: bool
    tester: bool
    lp: ProfileGetResponseLP
    notifications: bool
    last_ip: Optional[str]
    last_online: int
    req_time: int
    api: Optional[ProfileGetResponseApi]

    @property
    def last_online_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.last_online / 1000)

    @property
    def req_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.req_time / 1000)
    
    @property
    def premium_datetime(self) -> datetime:
        if isinstance(self.premium, bool):
            raise ValueError("User don't have premium")
        return datetime.fromtimestamp(self.premium / 1000)


    @property
    def premium_timedelta(self) -> timedelta:
        if isinstance(self.premium, bool):
            raise ValueError("User don't have premium")
        return datetime.fromtimestamp(self.premium / 1000) - datetime.now()

class ProfileGet(BaseModel):
    response: ProfileGetResponse
