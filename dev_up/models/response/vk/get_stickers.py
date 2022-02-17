import typing as ty

from pydantic import Field

from dev_up.base.models import ResponseModel


class VKGetStickersResponsePrice(ResponseModel):
    votes: int = Field(title="Стоимость в голосах")
    rub: int = Field(title="Стоимость в рублях")


class VKGetStickersResponseStickersItem(ResponseModel):
    id: int = Field(title="ID стикера")
    pack_id: int = Field(title="ID стикер-пака")
    name: str = Field(title="Имя стикер-пака")
    stickers_count: ty.Optional[int] = Field(title="Количество стикеров в стикер-паке [премиум]")
    author: ty.Optional[str] = Field(title="Информация об авторе стикер-пака [премиум]")
    description: ty.Optional[str] = Field(title="Описание стикер-пака [премиум]")
    photo: ty.Optional[str] = Field(title="URL стикер-пака [премиум]")
    price: ty.Optional[VKGetStickersResponsePrice] = Field(title="Цена стикер-пака [премиум]")
    url_buy: ty.Optional[str] = Field(title="Ссылка для покупки стикер-пака [премиум]")


class VKGetStickersResponse(ResponseModel):
    user_id: int = Field(title="ID пользователя")
    count: int = Field(title="Количество стикер-паков пользователя")
    count_all: int = Field(title="Количество стикер-паков в VK")
    stickers: ty.List[VKGetStickersResponseStickersItem] = Field(title="Список стикеров пользователя")
    price: ty.Optional[VKGetStickersResponsePrice] = Field(title="Цена всех стикеров [премиум]")
    system_comment: ty.Optional[str] = Field(title="Системное сообщение")
