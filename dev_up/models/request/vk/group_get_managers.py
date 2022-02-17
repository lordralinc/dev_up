import typing

from dev_up.base.models import RequestModel

__all__ = (
    'VKGroupGetManagersRequest',
)


class VKGroupGetManagersRequest(RequestModel):
    group_id: typing.Union[int, str]
