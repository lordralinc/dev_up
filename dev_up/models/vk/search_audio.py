from pydantic import BaseModel


class VkSearchAudioResponse(BaseModel):
    q: str
    count: int
    attachments: str
    msg_response: str


class VkSearchAudio(BaseModel):
    response: VkSearchAudioResponse
