from abc import abstractmethod
from typing import TYPE_CHECKING

from dev_up.abc import APICategoriesABC, BaseAPICategoriesABC
from dev_up.models import (
    VkGetStickersResponse,
    VkGetGroupsResponse,
    VkGetAppsResponse,
    ProfileGetResponse,
    AudioSpeechResponse
)

if TYPE_CHECKING:
    from dev_up.api import DevUpAPI


class BaseAPICategories(BaseAPICategoriesABC):

    def __init__(self, api: "DevUpAPI"):
        self.api = api


class VkAPICategories(BaseAPICategories):

    def get_stickers(self, user_id: int) -> VkGetStickersResponse:
        return VkGetStickersResponse(
            **self.api.make_request('vk.getStickers', dict(user_id=user_id))
        )

    def get_groups(self, user_id: int) -> VkGetGroupsResponse:
        return VkGetGroupsResponse(
            **self.api.make_request('vk.getGroups', dict(user_id=user_id))
        )

    def get_apps(self, user_id: int) -> VkGetAppsResponse:
        return VkGetAppsResponse(
            **self.api.make_request('vk.getApps', dict(user_id=user_id))
        )


class ProfileAPICategories(BaseAPICategories):

    def get(self):
        return ProfileGetResponse(
            **self.api.make_request('profile.get')
        )


class AudioAPICategories(BaseAPICategories):

    def speech(self, url: str) -> AudioSpeechResponse:
        return AudioSpeechResponse(
            **self.api.make_request('audio.speech', data=dict(url=url))
        )


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
    @abstractmethod
    def api_instance(self) -> "DevUpAPI":
        pass
