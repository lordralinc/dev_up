from pydantic import BaseModel

__all__ = (
    'AudioSpeechResponse',
    'AudioSpeech',
)


class AudioSpeechResponse(BaseModel):
    url: str
    text: str


class AudioSpeech(BaseModel):
    response: AudioSpeechResponse

