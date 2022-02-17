import typing as ty

from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'VKGetGroupsResponseGroupsItem',
    'VKGetGroupsResponseDescription',
    'VKGetGroupsResponse',
)


class VKGetGroupsResponseGroupsItem(ResponseModel):
    id: int = Field(title="ID", description="ID группы VK")
    name: str = Field(title="Имя", description="Имя группы VK")
    photo: str = Field(title="Фотография", description="Фотография (аватарка) группы VK")
    domain: ty.Optional[str] = Field(title="Домен", description="Часть URL группы VK")
    members_count: int = Field(title="Количество участников", description="Количество участников группы VK")
    verified: bool = Field(
        default_factory=bool,
        title="Верефицированое сообщество",
        description="Верефицированна ли группа VK"
    )

    @property
    def vk_link(self) -> str:
        if self.domain:
            return "https://vk.com/{domain}".format(domain=self.domain)
        return "https://vk.com/public{group_id}".format(group_id=self.id)


class VKGetGroupsResponseDescription(ResponseModel):
    ru: str = Field(title="Описание", description="Описание на русском языке")
    en: str = Field(title="Описание", description="Описание на английском языке")
    kz: str = Field(title="Описание", description="Описание на казахском языке")
    uk: str = Field(title="Описание", description="Описание на украинском языке")


class VKGetGroupsResponse(ResponseModel):
    user_id: int = Field(title="ID", description="ID владельца групп")
    count: int = Field(0, title="Количество", description="Количество групп")
    groups: ty.List[VKGetGroupsResponseGroupsItem] = Field([], title="Группы", description="Список групп")
    description: VKGetGroupsResponseDescription = Field(title="Описание", description="Описание на разных языках")
