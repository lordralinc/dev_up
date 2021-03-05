from pydantic import BaseModel


class ProfileGetBalanceLinkResponse(BaseModel):
    url: str


class ProfileGetBalanceLink(BaseModel):
    response: ProfileGetBalanceLinkResponse
