from dev_up.base.models import RequestModel

__all__ = (
    'VKExpertsGetInfoRequest',
)


class VKExpertsGetInfoRequest(RequestModel):
    user_id: int
