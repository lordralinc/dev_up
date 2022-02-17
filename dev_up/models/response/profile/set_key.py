from ipaddress import IPv4Address

from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'ProfileSetKeyResponse',
)


class ProfileSetKeyResponse(ResponseModel):
    user_id: int = Field(title="ID пользователя")
    ip: IPv4Address = Field(title="IP адресс")
    key: str = Field(title="Ключ доступа")
