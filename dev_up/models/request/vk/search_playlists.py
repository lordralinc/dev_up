from dev_up.base.models import RequestModel

__all__ = (
    'VKSearchPlaylistsRequest',
)


class VKSearchPlaylistsRequest(RequestModel):
    q: str
