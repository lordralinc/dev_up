from abc import ABC

from dev_up.abc.api import DevUpAPIABC
from dev_up.categories.audio import AudioAPICategory
from dev_up.categories.profile import ProfileAPICategory
from dev_up.categories.utils import UtilsAPICategory
from dev_up.categories.vk import VKAPICategory


class APICategories(DevUpAPIABC, ABC):

    @property
    def audio(self) -> "AudioAPICategory":
        return AudioAPICategory(self.get_instance())

    @property
    def profile(self) -> "ProfileAPICategory":
        return ProfileAPICategory(self.get_instance())

    @property
    def utils(self) -> "UtilsAPICategory":
        return UtilsAPICategory(self.get_instance())

    @property
    def vk(self) -> "VKAPICategory":
        return VKAPICategory(self.get_instance())
