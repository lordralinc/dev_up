from dev_up import ResponseModel, RequestModel


class PingRequest(RequestModel):
    ping: str

    __test__ = False


class PingResponse(ResponseModel):
    success: bool

    __test__ = False
