from typing import TYPE_CHECKING

from dev_up.abc import BaseAPICategoriesABC

if TYPE_CHECKING:
    from dev_up.api import DevUpAPI


class BaseAPICategories(BaseAPICategoriesABC):

    def __init__(self, api: "DevUpAPI"):
        self.api = api
