import pytest

from dev_up import JsonParser


@pytest.mark.asyncio
async def test_json_parsers_loads():
    _json = '{"response": true}'
    _dict = {"response": True}
    parser = JsonParser()
    assert parser.loads(_json) == _dict
    assert parser.dumps(_dict) == _json
