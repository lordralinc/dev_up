from typing import List, Optional

from pydantic import BaseModel


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
    count_all: int
    stickers: List[Sticker]
    price: Optional[StickersPrice] = None
    system_comment: Optional[str] = None


class VkGetStickers(BaseModel):
    response: VkGetStickersResponse
