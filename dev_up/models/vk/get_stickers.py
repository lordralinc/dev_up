from typing import List, Optional

from pydantic import BaseModel

__all__ = (
    'StickersPrice',
    'Sticker',
    'VkGetStickersResponse',
    'VkGetStickers',
)


class StickersPrice(BaseModel):
    votes: int
    rub: int


class Sticker(BaseModel):
    id: int
    pack_id: int
    name: str
    stickers_count: Optional[int] = None
    author: Optional[str] = None
    description: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[StickersPrice] = None
    url_buy: Optional[str] = None


class VkGetStickersResponse(BaseModel):
    user_id: int
    count: int
    stickers: List[Sticker]
    price: Optional[StickersPrice] = None


class VkGetStickers(BaseModel):
    response: VkGetStickersResponse
