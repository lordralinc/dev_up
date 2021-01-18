from abc import abstractmethod
from typing import TYPE_CHECKING

from dev_up.abc import APICategoriesABC, BaseAPICategoriesABC
from dev_up.models import (
    VkGetStickersResponse,
    VkGetGroupsResponse,
    VkGetAppsResponse,
    ProfileGetResponse,
    AudioSpeechResponse, UtilsMD5GenerateResponse, UtilsGetServerTimeResponse
)

if TYPE_CHECKING:
    from dev_up.api import DevUpAPI


class BaseAPICategories(BaseAPICategoriesABC):

    def __init__(self, api: "DevUpAPI"):
        self.api = api


class VkAPICategories(BaseAPICategories):

    def get_stickers(self, user_id: int) -> VkGetStickersResponse:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        """
        return self.api.make_request('vk.getStickers', dict(user_id=user_id), dataclass=VkGetStickersResponse)

    def get_groups(self, user_id: int) -> VkGetGroupsResponse:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        """
        return self.api.make_request('vk.getGroups', dict(user_id=user_id), dataclass=VkGetGroupsResponse)

    def get_apps(self, user_id: int) -> VkGetAppsResponse:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        """
        return self.api.make_request('vk.getApps', dict(user_id=user_id), dataclass=VkGetAppsResponse)

    async def get_stickers_async(self, user_id: int) -> VkGetStickersResponse:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        """
        return await self.api.make_request_async(
            'vk.getStickers',
            dict(user_id=user_id),
            dataclass=VkGetStickersResponse
        )

    async def get_groups_async(self, user_id: int) -> VkGetGroupsResponse:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        """
        return await self.api.make_request_async('vk.getGroups', dict(user_id=user_id), dataclass=VkGetGroupsResponse)

    async def get_apps_async(self, user_id: int) -> VkGetAppsResponse:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        """
        return await self.api.make_request_async('vk.getApps', dict(user_id=user_id), dataclass=VkGetAppsResponse)


class ProfileAPICategories(BaseAPICategories):

    def get(self):
        """Получает информацию о профиле DEV-UP"""
        return self.api.make_request('profile.get', dataclass=ProfileGetResponse)

    async def get_async(self):
        """Получает информацию о профиле DEV-UP"""
        return await self.api.make_request_async('profile.get', dataclass=ProfileGetResponse)


class AudioAPICategories(BaseAPICategories):

    def speech(self, url: str) -> AudioSpeechResponse:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        """
        return self.api.make_request('audio.speech', dict(url=url), dataclass=AudioSpeechResponse)

    async def speech_async(self, url: str) -> AudioSpeechResponse:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        """
        return await self.api.make_request_async('audio.speech', dict(url=url), dataclass=AudioSpeechResponse)


class UtilsAPICategories(BaseAPICategories):

    def md5_generate(self, text: str) -> UtilsMD5GenerateResponse:
        """Получить хэш md5 из текста

        :param text: текст
        """
        return self.api.make_request('utils.md5Generate', dict(text=text), dataclass=UtilsMD5GenerateResponse)

    def get_server_time(self) -> UtilsGetServerTimeResponse:
        """Возвращает текущее время на сервере в unixtime (МСК)"""
        return self.api.make_request("utils.getServerTime", dataclass=UtilsGetServerTimeResponse)

    async def md5_generate_async(self, text: str) -> UtilsMD5GenerateResponse:
        """Получить хэш md5 из текста

        :param text: текст
        """
        return await self.api.make_request_async(
            'utils.md5Generate',
            dict(text=text),
            dataclass=UtilsMD5GenerateResponse
        )

    async def get_server_time_async(self) -> UtilsGetServerTimeResponse:
        """Возвращает текущее время на сервере в unixtime (МСК)"""
        return await self.api.make_request_async("utils.getServerTime", dataclass=UtilsGetServerTimeResponse)


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
