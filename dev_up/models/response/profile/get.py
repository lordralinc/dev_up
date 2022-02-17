import typing as ty
from datetime import datetime, timedelta
from ipaddress import IPv4Address

from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'ProfileGetResponseApi',
    'ProfileGetResponseLP',
    'ProfileGetResponse',
)


class ProfileGetResponseApi(ResponseModel):
    key: str = Field(title="Ключ доступа")
    balance: float = Field(title="Текущий баланс")
    limit: int = Field(title="Лимит на месяц")
    rate_limit: int = Field(title="Лимит на день")
    warn: int = Field(title="Количество предупреждений")
    used: int = Field(title="Количество использований")


class ProfileGetResponseLP(ResponseModel):
    created: bool = Field(False, title="Создан ли ЛП")
    status: bool = Field(False, title="Запущен ли ЛП")


class ProfileGetResponse(ResponseModel):
    id: int = Field(title="ID")
    id_vk: int = Field(title="ID VK")
    first_name: str = Field(title="Имя")
    last_name: str = Field(title="Фамилия")
    last_ip: ty.Optional[IPv4Address] = Field(title="Последний IP адресс")
    last_online: int = Field(title="Последний онлайн")
    req_time: int = Field(title="unknown")
    api: ty.Optional[ProfileGetResponseApi] = Field(title="Информация об API")
    verified: int = Field(False, title="Подтвержден ли аккаунт")
    notifications: bool = Field(False, title="Включены ли уведомления")
    premium: ty.Union[int, bool] = Field(False, title="Премиум")
    unlimited: bool = Field(False, title="Безлимитные запросы")
    ban: bool = Field(False, title="Заблокирован ли")
    banip: bool = Field(False, title="Заблокирован ли по IP")
    tester: bool = Field(False, title="Является ли тестером")

    lp: ProfileGetResponseLP = Field(ProfileGetResponseLP(), title="Информация об ЛП")

    @property
    def last_online_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.last_online / 1000)

    @property
    def req_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.req_time / 1000)

    @property
    def have_premium(self) -> bool:
        return not (isinstance(self.premium, bool) or self.premium == 0)

    @property
    def premium_datetime(self) -> datetime:
        if not self.have_premium:
            raise ValueError("User don't have premium")
        return datetime.fromtimestamp(self.premium / 1000)

    @property
    def premium_timedelta(self) -> timedelta:
        return self.premium_datetime - datetime.now()
