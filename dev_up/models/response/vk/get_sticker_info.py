import typing as ty

from pydantic import Field

from dev_up.base.models import ResponseModel

__all__ = (
    'VKGetStickerInfoResponseStickerImagesItem',
    'VKGetStickerInfoResponseStickerHints',
    'VKGetStickerInfoResponseSticker',
    'VKGetStickerInfoResponsePackPriceDiscountValues',
    'VKGetStickerInfoResponsePackPriceDiscount',
    'VKGetStickerInfoResponsePackPrice',
    'VKGetStickerInfoResponsePack',
    'VKGetStickerInfoResponse',
)


class VKGetStickerInfoResponseStickerImagesItem(ResponseModel):
    url: str = Field(title="URL фотографии")
    width: int = Field(title="Ширина фотографии")
    height: int = Field(title="Высота фотографии")


class VKGetStickerInfoResponseStickerHints(ResponseModel):
    count: int = Field(title="Количество подсказок")
    items: ty.List[str] = Field(title="Список подсказок")


class VKGetStickerInfoResponseSticker(ResponseModel):
    id: int = Field(title="ID стикера")
    images: ty.List[VKGetStickerInfoResponseStickerImagesItem] = Field(title="Список изображений")
    hints: VKGetStickerInfoResponseStickerHints = Field(title="Подсказки ко стикеру")


class VKGetStickerInfoResponsePackPriceDiscountValues(ResponseModel):
    old: int = Field(title="Старая цена")
    installed: int = Field(title="Новая цена")


class VKGetStickerInfoResponsePackPriceDiscount(ResponseModel):
    price_buy_discount: str = Field(title="Описание скидки")
    votes: ty.Optional[VKGetStickerInfoResponsePackPriceDiscountValues] = Field(title="Стоимость в голосах")
    rub: ty.Optional[VKGetStickerInfoResponsePackPriceDiscountValues] = Field(title="Стоимость в рублях")


class VKGetStickerInfoResponsePackPrice(ResponseModel):
    votes: int = Field(title="Стоимость в голосах")
    rub: int = Field(title="Стоимость в рублях")
    discount: ty.Optional[VKGetStickerInfoResponsePackPriceDiscount] = Field(title="Скидка")


class VKGetStickerInfoResponsePack(ResponseModel):
    id: int = Field(title="ID стикер-пака")
    title: str = Field(title="Имя стикер-пака")
    stickers_count: int = Field(0, title="Количество стикеров в стикер-пака")
    price: ty.Optional[VKGetStickerInfoResponsePackPrice] = Field(title="Информация о стоимости стикер-пака")
    author: ty.Optional[str] = Field(title="Информация об авторе стикер-пака [премиум]")
    description: ty.Optional[str] = Field(title="Описание стикер-пака [премиум]")


class VKGetStickerInfoResponse(ResponseModel):
    sticker: VKGetStickerInfoResponseSticker = Field(title="Информация о стикере")
    pack: VKGetStickerInfoResponsePack = Field(title="Информация о стикер-паке")
    system_comment: ty.Optional[str] = Field(None, title="Системный комментарий")
