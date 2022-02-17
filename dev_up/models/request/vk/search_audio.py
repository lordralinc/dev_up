from dev_up.base.models import RequestModel

__all__ = (
    'VKSearchAudioRequest',
)


class VKSearchAudioRequest(RequestModel):
    q: str
