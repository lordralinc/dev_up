from abc import abstractmethod
from typing import TYPE_CHECKING, Union
from dev_up.abc import APICategoriesABC, BaseAPICategoriesABC
from dev_up import models

if TYPE_CHECKING:
    from dev_up.api import DevUpAPI


class BaseAPICategories(BaseAPICategoriesABC):

    def __init__(self, api: "DevUpAPI"):
        self.api = api


class VkAPICategories(BaseAPICategories):

    def get_stickers(self, user_id: int) -> models.VkGetStickers:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        """
        return self.api.make_request(
            method='vk.getStickers',
            data=dict(user_id=user_id),
            dataclass=models.VkGetStickers
        )

    def get_sticker_info(self, sticker_id: int) -> models.VkGetStickerInfo:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        """
        return self.api.make_request(
            method='vk.getStickerInfo',
            data=dict(sticker_id=sticker_id),
            dataclass=models.VkGetStickerInfo
        )

    def get_groups(self, user_id: int) -> models.VkGetGroups:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        """
        return self.api.make_request(
            method='vk.getGroups',
            data=dict(user_id=user_id),
            dataclass=models.VkGetGroups
        )

    def get_apps(self, user_id: int) -> models.VkGetApps:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        """
        return self.api.make_request(
            method='vk.getApps',
            data=dict(user_id=user_id),
            dataclass=models.VkGetApps
        )

    async def get_stickers_async(self, user_id: int) -> models.VkGetStickers:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        """
        return await self.api.make_request_async(
            method='vk.getStickers',
            data=dict(user_id=user_id),
            dataclass=models.VkGetStickers
        )

    async def get_sticker_info_async(self, sticker_id: int) -> models.VkGetStickerInfo:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        """
        return await self.api.make_request_async(
            method='vk.getStickerInfo',
            data=dict(sticker_id=sticker_id),
            dataclass=models.VkGetStickerInfo
        )

    async def get_groups_async(self, user_id: int) -> models.VkGetGroups:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        """
        return await self.api.make_request_async(
            method='vk.getGroups',
            data=dict(user_id=user_id),
            dataclass=models.VkGetGroups
        )

    async def get_apps_async(self, user_id: int) -> models.VkGetApps:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        """
        return await self.api.make_request_async(
            method='vk.getApps',
            data=dict(user_id=user_id),
            dataclass=models.VkGetApps
        )


class ProfileAPICategories(BaseAPICategories):

    def get(self) -> models.ProfileGet:
        """Получает информацию о профиле DEV-UP"""
        return self.api.make_request(
            method='profile.get',
            data=dict(),
            dataclass=models.ProfileGet
        )

    async def get_async(self) -> models.ProfileGet:
        """Получает информацию о профиле DEV-UP"""
        return await self.api.make_request_async(
            method='profile.get',
            data=dict(),
            dataclass=models.ProfileGet
        )


class AudioAPICategories(BaseAPICategories):

    def speech(self, url: str) -> models.AudioSpeech:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        """
        return self.api.make_request(
            method='audio.speech',
            data=dict(url=url),
            dataclass=models.AudioSpeech
        )

    async def speech_async(self, url: str) -> models.AudioSpeech:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        """
        return await self.api.make_request_async(
            method='audio.speech',
            data=dict(url=url),
            dataclass=models.AudioSpeech
        )


class UtilsAPICategories(BaseAPICategories):

    def md5_generate(self, text: str) -> models.UtilsMD5Generate:
        """Получить хэш md5 из текста

        :param text: текст
        """
        return self.api.make_request(
            method='utils.md5Generate',
            data=dict(text=text),
            dataclass=models.UtilsMD5Generate
        )

    def get_server_time(self) -> models.UtilsGetServerTime:
        """Возвращает текущее время на сервере в unixtime (МСК)"""
        return self.api.make_request(
             method="utils.getServerTime",
             data=dict(),
             dataclass=models.UtilsGetServerTime
        )

    def get_short_link(self, url: str) -> models.UtilsGetShortLink:
        """Сокращение ссылок"""
        return self.api.make_request(
            method="utils.getShortLink",
            data=dict(url=url),
            dataclass=models.UtilsGetShortLink
        )

    def notifications_links(
            self,
            code: str,
            status: Union[int, models.NotificationsLinksStatus]
    ) -> models.UtilsNotificationsLinks:
        """Управление уведомлениями от ссылок"""
        return self.api.make_request(
            method="utils.notificationsLinks",
            data=dict(code=code, status=models.NotificationsLinksStatus(status).value),
            dataclass=models.UtilsNotificationsLinks
        )

    async def md5_generate_async(self, text: str) -> models.UtilsMD5Generate:
        """Получить хэш md5 из текста

        :param text: текст
        """
        return await self.api.make_request_async(
            method='utils.md5Generate',
            data=dict(text=text),
            dataclass=models.UtilsMD5Generate
        )

    async def get_server_time_async(self) -> models.UtilsGetServerTime:
        """Возвращает текущее время на сервере в unixtime (МСК)"""
        return await self.api.make_request_async(
            method="utils.getServerTime",
            data=dict(),
            dataclass=models.UtilsGetServerTime
        )

    async def get_short_link_async(self, url: str) -> models.UtilsGetShortLink:
        """Сокращение ссылок"""
        return await self.api.make_request_async(
            method="utils.getShortLink",
            data=dict(url=url),
            dataclass=models.UtilsGetShortLink
        )

    async def notifications_links_async(
            self,
            code: str,
            status: Union[int, models.NotificationsLinksStatus]
    ) -> models.UtilsNotificationsLinks:
        """Управление уведомлениями от ссылок"""
        return await self.api.make_request_async(
            method="utils.notificationsLinks",
            data=dict(code=code, status=models.NotificationsLinksStatus(status).value),
            dataclass=models.UtilsNotificationsLinks
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
    def utils(self) -> UtilsAPICategories:
        return UtilsAPICategories(self.api_instance)

    @property
    @abstractmethod
    def api_instance(self) -> "DevUpAPI":
        pass
