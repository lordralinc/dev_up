from pydantic import Field

from dev_up.base.models import RequestModel

__all__ = (
    'AudioSpeechRequest',
)


class AudioSpeechRequest(RequestModel):
    url: str = Field(title="URL MP3 файла")
