import typing

from dev_up.abc.category import APICategoryABC

if typing.TYPE_CHECKING:
    from dev_up import DevUpAPI, DevUpAPIABC


class APICategory(APICategoryABC):

    def __init__(self, api: "DevUpAPIABC"):
        self._api = api

    @property
    def api(self) -> "DevUpAPI":
        return self._api
