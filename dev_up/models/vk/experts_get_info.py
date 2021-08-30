import typing as ty
from pydantic import BaseModel

class VkExpertsGetInfoResponseItemInfo(BaseModel):
    actions_count: int
    position: int
    topic_name: str
    user_id: int

class VkExpertsGetInfoResponseItem(BaseModel):
    info: VkExpertsGetInfoResponseItemInfo
    is_expert: bool

class VkExpertsGetInfoResponse(BaseModel):
    count: int
    items: ty.List[VkExpertsGetInfoResponseItem]


class VkExpertsGetInfo(BaseModel):
    response: VkExpertsGetInfoResponse
