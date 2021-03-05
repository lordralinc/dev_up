from typing import List, Optional

from pydantic import BaseModel

from dev_up.models import Description


class Group(BaseModel):
    id: int
    name: str
    photo: str
    domain: str
    members_count: int
    verified: int


class VkGetGroupsResponse(BaseModel):
    user_id: int
    count: int
    groups: Optional[List[Group]]
    description: Description


class VkGetGroups(BaseModel):
    response: VkGetGroupsResponse
