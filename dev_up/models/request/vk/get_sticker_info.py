from dev_up.base.models import RequestModel

__all__ = (
    'VKGetStickerInfoRequest',
)


class VKGetStickerInfoRequest(RequestModel):
    sticker_id: int
