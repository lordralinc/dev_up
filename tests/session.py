import typing as ty

from dev_up import SessionABC, JsonParser, DevUpAPI


def url_gen(method: str) -> str:
    return "https://api.{base_url}/method/{method}".format(
        base_url=DevUpAPI.base_url,
        method=method
    )


def data_gen(response: ty.Any) -> ty.Dict[str, ty.Any]:
    return dict(response=response)


class TestSession(SessionABC):
    methods = {
        url_gen('test'): data_gen({"success": True})
    }

    def __init__(self):
        self._json_parser = JsonParser()

    async def close(self) -> ty.NoReturn:
        pass

    async def make_post_request(self, url: str, data: ty.Optional[ty.Dict[str, ty.Any]]) -> ty.Any:
        return self._json_parser.dumps(self.methods[url])

    async def make_json(self, url: str, data: ty.Optional[ty.Dict[str, ty.Any]]) -> ty.Union[ty.Dict, ty.List]:
        return self._json_parser.loads(await self.make_post_request(url, data))

    __test__ = False
