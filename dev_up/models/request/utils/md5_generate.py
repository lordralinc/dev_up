from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'UtilsMD5GenerateRequest',
)


class UtilsMD5GenerateRequest(RequestModel):
    text: str = Field(title="Текст")
