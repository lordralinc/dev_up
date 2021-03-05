from typing import List, Optional

from pydantic import BaseModel


class VkGetStickerInfoResponseStickerImage(BaseModel):
    url: str
    width: int
    height: int


class VkGetStickerInfoResponseStickerHints(BaseModel):
    count: int
    items: List[str]


class DiscountValues(BaseModel):
    old: int
    installed: int


class Discount(BaseModel):
    price_buy_discount: str
    votes: Optional[DiscountValues]
    rub: Optional[DiscountValues]


class VkGetStickerInfoResponsePackPrice(BaseModel):
    votes: int
    rub: int
    discount: Optional[Discount]


class VkGetStickerInfoResponseSticker(BaseModel):
    id: int
    images: Optional[List[VkGetStickerInfoResponseStickerImage]]
    hints: Optional[VkGetStickerInfoResponseStickerHints]


class VkGetStickerInfoResponsePack(BaseModel):
    id: int
    title: str
    stickers_count: Optional[int] = 0
    price: Optional[VkGetStickerInfoResponsePackPrice]
    author: Optional[str] = "Только с премиум доступом"
    description: Optional[str] = "Только с премиум доступом"


class VkGetStickerInfoResponse(BaseModel):
    sticker: VkGetStickerInfoResponseSticker
    pack: VkGetStickerInfoResponsePack
    system_comment: Optional[str] = None


class VkGetStickerInfo(BaseModel):
    response: VkGetStickerInfoResponse
