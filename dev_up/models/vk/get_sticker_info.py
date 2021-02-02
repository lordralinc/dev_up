from typing import List, Optional

from pydantic import BaseModel

__all__ = (
    'VkGetStickerInfoResponseStickerImage',
    'VkGetStickerInfoResponseStickerHints',
    'DiscountValues',
    'Discount',
    'VkGetStickerInfoResponsePackPrice',
    'VkGetStickerInfoResponseSticker',
    'VkGetStickerInfoResponsePack',
    'VkGetStickerInfoResponse',
    'VkGetStickerInfo',
)


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
    stickers_count: int
    price: Optional[VkGetStickerInfoResponsePackPrice]
    author: str
    description: str


class VkGetStickerInfoResponse(BaseModel):
    sticker: VkGetStickerInfoResponseSticker
    pack: VkGetStickerInfoResponsePack


class VkGetStickerInfo(BaseModel):
    response: VkGetStickerInfoResponse
