import typing as ty
from pydantic import BaseModel



class VkTestersGetInfoResponseBugreports(BaseModel):
    count: int
    items: ty.List[dict]


class VkTestersGetInfoResponseProducts(BaseModel):
    available_products_count: int
    items: ty.List[dict]
    secret_products_count: int
    secret_reports_count: int
    uncounted_reports_count: int
    unshown_reports_count: int


class VkTestersGetInfoResponseUserInfo(BaseModel):
    id: int
    first_name: str
    last_name: str
    is_closed: bool
    reports_count: int
    status_text: str
    top_position: int


class VkTestersGetInfoResponse(BaseModel):
    bugreports: VkTestersGetInfoResponseBugreports
    products: VkTestersGetInfoResponseProducts
    user_info: VkTestersGetInfoResponseUserInfo
    is_tester: bool


class VkTestersGetInfo(BaseModel):
    response: VkTestersGetInfoResponse
