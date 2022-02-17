from pydantic import Field, AnyUrl

from dev_up.base.models import ResponseModel

__all__ = (
    'AudioSpeechResponse',
)


class AudioSpeechResponse(ResponseModel):
    url: AnyUrl = Field(title="URL MP3 файла")
    text: str = Field(title="Распознанный текст")
