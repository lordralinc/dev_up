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
    created: bool = False
    status: bool = False


class ProfileGetResponse(BaseModel):
    id: int
    id_vk: int
    first_name: str
    last_name: str 
    last_ip: Optional[str]
    last_online: int
    req_time: int
    api: Optional[ProfileGetResponseApi]
    verified: int = False    
    notifications: bool = False
    premium: Union[int, bool] = False
    unlimited: bool = False
    ban: bool = False
    banip: bool = False
    tester: bool = False

    lp: ProfileGetResponseLP = ProfileGetResponseLP()

    @property
    def last_online_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.last_online / 1000)

    @property
    def req_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.req_time / 1000)

    @property
    def have_premium(self) -> bool:
        return not (isinstance(self.premium, bool) or self.premium == 0)
    
    @property
    def premium_datetime(self) -> datetime:
        if not self.have_premium:
            raise ValueError("User don't have premium")
        return datetime.fromtimestamp(self.premium / 1000)

    @property
    def premium_timedelta(self) -> timedelta:
        return self.premium_datetime - datetime.now()

class ProfileGet(BaseModel):
    response: ProfileGetResponse
