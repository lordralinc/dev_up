import typing as ty

from pydantic import BaseModel


class VkGrouGetManagersResponseManager(BaseModel):
    id: int
    name: str
    photo: str
    domain: str
    followers_count: int
    status: str
    verified: bool
    from_app: bool


class VkGrouGetManagersResponse(BaseModel):
    group_id: ty.Union[str, int]
    count: int
    managers: ty.List[VkGrouGetManagersResponseManager]

class VkGrouGetManagers(BaseModel):
    response: VkGrouGetManagersResponse
