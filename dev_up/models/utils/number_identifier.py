from pydantic import BaseModel


class UtilsNumberIdentifierResponseGeo(BaseModel):
    region: str


class UtilsNumberIdentifierResponse(BaseModel):
    number: str
    operator: str
    operator_id: str
    geo: UtilsNumberIdentifierResponseGeo


class UtilsNumberIdentifier(BaseModel):
    response: UtilsNumberIdentifierResponse
