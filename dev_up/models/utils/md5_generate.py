from pydantic import BaseModel


class UtilsMD5GenerateResponse(BaseModel):
    date: str


class UtilsMD5Generate(BaseModel):
    response: UtilsMD5GenerateResponse
