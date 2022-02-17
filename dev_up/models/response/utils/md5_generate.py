from dev_up.base.models import ResponseModel

__all__ = (
    'UtilsMD5GenerateResponse',
)


class UtilsMD5GenerateResponse(ResponseModel):
    hash: str
