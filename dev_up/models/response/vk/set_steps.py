import datetime

from dev_up.base.models import ResponseModel


class VKSetStepsResponse(ResponseModel):
    date: str
    steps: int
    distance: int

    @property
    def date_dt(self) -> datetime.datetime:
        return datetime.datetime.strptime(self.date, "%Y-%m-%d")
