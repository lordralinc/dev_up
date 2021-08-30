from pydantic import BaseModel


class VkSearchPlaylistsResponse(BaseModel):
    q: str
    count: int
    attachments: str
    msg_response: str


class VkSearchPlaylists(BaseModel):
    response: VkSearchPlaylistsResponse
