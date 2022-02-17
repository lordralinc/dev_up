from dev_up.base.models import ResponseModel


class VKSearchPlaylistsResponse(ResponseModel):
    q: str
    count: int
    attachments: str
    msg_response: str
