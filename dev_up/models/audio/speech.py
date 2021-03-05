from pydantic import BaseModel


class AudioSpeechResponse(BaseModel):
    url: str
    text: str


class AudioSpeech(BaseModel):
    response: AudioSpeechResponse
