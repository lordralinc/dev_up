import pytest

from dev_up import DevUpAPI
from tests.models import PingRequest, PingResponse
from tests.session import TestSession


@pytest.mark.asyncio
async def test_make_request():
    _test_access_token = "111"
    _data = {'ping': '111'}

    api = DevUpAPI(
        access_token=_test_access_token,
        session=TestSession()
    )
    _url = api.default_url_generator('test')
    raw_response = await api.make_request(
        'test',
        _data,
        raw_response=True
    )
    response = await api.make_request(
        'test',
        _data
    )
    response_with_validation = await api.make_request(
        'test',
        _data,
        request_model=PingRequest,
        response_model=PingResponse
    )

    _answer = TestSession.methods[_url]

    assert raw_response == _answer
    assert response == _answer['response']
    assert response_with_validation == PingResponse.parse_obj(_answer['response'])
