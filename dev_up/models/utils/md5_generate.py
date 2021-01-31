from pydantic import BaseModel

__all__ = (
    'UtilsMD5GenerateResponse',
    'UtilsMD5Generate',
)


class UtilsMD5GenerateResponse(BaseModel):
    date: str


class UtilsMD5Generate(BaseModel):
    response: UtilsMD5GenerateResponse
