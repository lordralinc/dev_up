import typing as ty

from dev_up.base.models import ResponseModel


class VKTestersGetInfoResponseBugreports(ResponseModel):
    count: int
    items: ty.List[dict]


class VKTestersGetInfoResponseProducts(ResponseModel):
    available_products_count: int
    items: ty.List[dict]
    secret_products_count: int
    secret_reports_count: int
    uncounted_reports_count: int
    unshown_reports_count: int


class VKTestersGetInfoResponseUserInfo(ResponseModel):
    id: int
    first_name: str
    last_name: str
    is_closed: bool
    reports_count: int
    status_text: str
    top_position: int


class VKTestersGetInfoResponse(ResponseModel):
    bugreports: VKTestersGetInfoResponseBugreports
    products: VKTestersGetInfoResponseProducts
    user_info: VKTestersGetInfoResponseUserInfo
    is_tester: bool
