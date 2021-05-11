from pydantic import BaseModel


class ProfileSetKeyResponse(BaseModel):
    user_id: int
    ip: str
    key: str


class ProfileSetKey(BaseModel):
    response: ProfileSetKeyResponse
