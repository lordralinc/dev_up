from typing import List, Optional

from pydantic import BaseModel

from dev_up.models import Description


class App(BaseModel):
    id: int
    name: str
    photo: str
    domain: str
    members_count: int


class VkGetAppsResponse(BaseModel):
    user_id: int
    count: int
    apps: Optional[List[App]]
    description: Description


class VkGetApps(BaseModel):
    response: VkGetAppsResponse
