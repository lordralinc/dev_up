from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'VKSetStepsRequest',
)


class VKSetStepsRequest(RequestModel):
    access_token: str = Field(max_length=85)
