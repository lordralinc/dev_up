import typing as ty


class DevUpException(Exception):

    def __repr__(self):
        return "<DevUpException:unknown>"


class DevUpResponseException(DevUpException):

    def __init__(
            self,
            url: str,
            err_code: int,
            err_critical_lvl: str = "",
            err_msg: str = "",
            params: ty.Optional[ty.List[ty.Dict[str, ty.Any]]] = None
    ):
        self.url = url
        self.err_code = err_code
        self.err_critical_lvl = err_critical_lvl
        self.err_msg = err_msg

        self.params = params or []

    def __repr__(self):
        return f"<DevUpResponseException:{self.err_critical_lvl.upper()}, code={self.err_code}, msg={self.err_msg}>"

    def __str__(self):
        return f"[{self.err_code}] {self.err_msg}"
