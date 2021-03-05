from pydantic import BaseModel


class ProfileBuyLimitResponse(BaseModel):
    success: bool


class ProfileBuyLimit(BaseModel):
    response: ProfileBuyLimitResponse
