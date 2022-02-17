import typing as ty

from dev_up.base.models import RequestModel

__all__ = (
    'ProfileGetRequest',

)


class ProfileGetRequest(RequestModel):
    user_id: ty.Optional[int] = None
