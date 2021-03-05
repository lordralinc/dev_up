from pydantic import BaseModel


class ProfileBuyPremiumResponse(BaseModel):
    success: bool


class ProfileBuyPremium(BaseModel):
    response: ProfileBuyPremiumResponse
