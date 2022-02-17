import json
import typing as ty

from dev_up.abc.json import JsonParserABC


class JsonParser(JsonParserABC):
    def dumps(self, data: ty.Dict[str, ty.Any]) -> str:
        return json.dumps(data)

    def loads(self, data: ty.Union[str, bytes]) -> ty.Dict[str, ty.Any]:
        return json.loads(data)
