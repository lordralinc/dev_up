from typing import List, Dict, Any


class DevUpException(Exception):

    def __init__(
            self,
            err_code: int,
            err_critical_lvl: str = "",
            err_msg: str = "",
            params: List[Dict[str, Any]] = None
    ):
        if params is None:
            params = []
        self.err_code = err_code
        self.err_critical_lvl = err_critical_lvl
        self.err_msg = err_msg

        self.params = params

    def __repr__(self):
        return f"<DevUpException:{self.err_critical_lvl.upper()}, code={self.err_code}, msg={self.err_msg}>"

    def __str__(self):
        return f"[{self.err_code}] {self.err_msg}"
