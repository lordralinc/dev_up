from dev_up.base.models import ResponseModel


class VKSearchAudioResponse(ResponseModel):
    q: str
    count: int
    attachments: str
    msg_response: str
