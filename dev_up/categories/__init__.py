from abc import abstractmethod
from typing import TYPE_CHECKING

from dev_up.abc import APICategoriesABC
from dev_up.categories.audio import AudioAPICategories
from dev_up.categories.profile import ProfileAPICategories
from dev_up.categories.utils import UtilsAPICategories
from dev_up.categories.vk import VkAPICategories

if TYPE_CHECKING:
    from dev_up import DevUpAPI


class APICategories(APICategoriesABC):

    @property
    def vk(self) -> VkAPICategories:
        return VkAPICategories(self.api_instance)

    @property
    def profile(self) -> ProfileAPICategories:
        return ProfileAPICategories(self.api_instance)

    @property
    def audio(self) -> AudioAPICategories:
        return AudioAPICategories(self.api_instance)

    @property
    def utils(self) -> UtilsAPICategories:
        return UtilsAPICategories(self.api_instance)

    @property
    @abstractmethod
    def api_instance(self) -> "DevUpAPI":
        pass
