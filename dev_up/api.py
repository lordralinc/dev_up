import requests

from dev_up.abc import DevUpAPIABC
from dev_up.categories import APICategories
from dev_up.exceptions import DevUpException


class DevUpAPI(DevUpAPIABC, APICategories):

    @property
    def api_instance(self) -> "DevUpAPI":
        return self

    def __init__(
            self,
            token: str
    ):
        self._token = token

    def make_request(
            self,
            method: str,
            data=None
    ) -> dict:
        if data is None:
            data = dict()
        data.update(key=self._token)
        response = requests.post(f"https://api.dev-up.ru/method/{method}", data=data).json()

        if 'err' in response:
            raise DevUpException(
                params=response['params'],
                **response['err']
            )

        return response
