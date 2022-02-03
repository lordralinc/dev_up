import datetime

from pydantic import BaseModel


class VkSetStepsResponse(BaseModel):
    date: str
    steps: int
    distance: int

    @property
    def date_dt(self) -> datetime.datetime:
        return datetime.datetime.strptime(self.date, "%Y-%m-%d")


class VkSetSteps(BaseModel):
    response: VkSetStepsResponse
