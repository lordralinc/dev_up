import typing as ty

from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'VKGetAppsResponseAppsItem',
    'VKGetAppsResponseDescription',
    'VKGetAppsResponse',
)


class VKGetAppsResponseAppsItem(ResponseModel):
    id: int = Field(title="ID", description="ID приложения VK")
    name: str = Field(title="Имя", description="Имя приложения VK")
    photo: str = Field(title="Фотография", description="Фотография (аватарка) приложения VK")
    domain: ty.Optional[str] = Field(title="Домен", description="Часть URL приложения VK")
    members_count: int = Field(title="Количество участников", description="Количество участников приложения VK")

    def vk_link(self) -> str:
        if self.domain:
            return "https://vk.com/{domain}".format(domain=self.domain)
        return "https://vk.com/app{app_id}".format(app_id=self.id)


class VKGetAppsResponseDescription(ResponseModel):
    ru: str = Field(title="Описание", description="Описание на русском языке")
    en: str = Field(title="Описание", description="Описание на английском языке")
    kz: str = Field(title="Описание", description="Описание на казахском языке")
    uk: str = Field(title="Описание", description="Описание на украинском языке")


class VKGetAppsResponse(ResponseModel):
    user_id: int = Field(title="ID", description="ID владельца приложений")
    count: int = Field(0, title="Количество", description="Количество приложений")
    apps: ty.List[VKGetAppsResponseAppsItem] = Field([], title="Приложения", description="Список приложений")
    description: VKGetAppsResponseDescription = Field(title="Описание", description="Описание на разных языках")
