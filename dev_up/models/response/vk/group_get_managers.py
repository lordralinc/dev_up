import typing as ty

from dev_up.base.models import ResponseModel


class VKGroupGetManagersResponseManager(ResponseModel):
    id: int
    name: str
    photo: str
    domain: str
    followers_count: int
    status: str
    verified: bool
    from_app: bool


class VKGroupGetManagersResponse(ResponseModel):
    group_id: ty.Union[str, int]
    count: int
    managers: ty.List[VKGroupGetManagersResponseManager]
