import typing as ty

from dev_up.base.models import ResponseModel


class VKExpertsGetInfoResponseItemInfo(ResponseModel):
    actions_count: int
    position: int
    topic_name: str
    user_id: int


class VKExpertsGetInfoResponseItem(ResponseModel):
    info: VKExpertsGetInfoResponseItemInfo
    is_expert: bool


class VKExpertsGetInfoResponse(ResponseModel):
    count: int
    items: ty.List[VKExpertsGetInfoResponseItem]
