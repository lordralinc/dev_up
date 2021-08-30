from dev_up import models
from dev_up.categories.base import BaseAPICategories


class VkAPICategories(BaseAPICategories):

    def get_stickers(self, user_id: int, key: str = None, **kwargs) -> models.VkGetStickers:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getStickers',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkGetStickers
        )

    def get_sticker_info(self, sticker_id: int, key: str = None, **kwargs) -> models.VkGetStickerInfo:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getStickerInfo',
            data=dict(sticker_id=sticker_id, key=key, **kwargs),
            dataclass=models.VkGetStickerInfo
        )

    def get_groups(self, user_id: int, key: str = None, **kwargs) -> models.VkGetGroups:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getGroups',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkGetGroups
        )

    def get_apps(self, user_id: int, key: str = None, **kwargs) -> models.VkGetApps:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getApps',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkGetApps
        )

    def search_playlists(self, q: str, key: str = None, **kwargs) -> models.VkSearchPlaylists:
        """Получает список плейлистов

        :param q: Поисковая строка
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.searchPlaylists',
            data=dict(q=q, key=key, **kwargs),
            dataclass=models.VkSearchPlaylists
        )
    
    def search_audio(self, q: str, key: str = None, **kwargs) -> models.VkSearchAudio:
        """Получает список аудиозаписей

        :param q: Поисковая строка
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.searchAudio',
            data=dict(q=q, key=key, **kwargs),
            dataclass=models.VkSearchAudio
        )

    def testers_get_info(self, user_id: int, key: str = None, **kwargs) -> models.VkTestersGetInfo:
        """Получает информацио о пользователе в программе VK Testers

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.testersGetInfo',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkTestersGetInfo
        )

    def experts_get_info(self, user_id: int, key: str = None, **kwargs) -> models.VkTestersGetInfo:
        """Получает информацио о пользователе в программе VK Experts

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.expertsGetInfo',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkTestersGetInfo
        )


    async def get_stickers_async(self, user_id: int, key: str = None, **kwargs) -> models.VkGetStickers:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getStickers',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkGetStickers
        )

    async def get_sticker_info_async(self, sticker_id: int, key: str = None, **kwargs) -> models.VkGetStickerInfo:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getStickerInfo',
            data=dict(sticker_id=sticker_id, key=key, **kwargs),
            dataclass=models.VkGetStickerInfo
        )

    async def get_groups_async(self, user_id: int, key: str = None, **kwargs) -> models.VkGetGroups:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getGroups',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkGetGroups
        )

    async def get_apps_async(self, user_id: int, key: str = None, **kwargs) -> models.VkGetApps:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getApps',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkGetApps
        )

    async def search_playlists_async(self, q: str, key: str = None, **kwargs) -> models.VkSearchPlaylists:
        """Получает список плейлистов

        :param q: Поисковая строка
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.searchPlaylists',
            data=dict(q=q, key=key, **kwargs),
            dataclass=models.VkSearchPlaylists
        )
    
    async def search_audio_async(self, q: str, key: str = None, **kwargs) -> models.VkSearchAudio:
        """Получает список аудиозаписей

        :param q: Поисковая строка
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.searchAudio',
            data=dict(q=q, key=key, **kwargs),
            dataclass=models.VkSearchAudio
        )

    async def testers_get_info_async(self, user_id: int, key: str = None, **kwargs) -> models.VkTestersGetInfo:
        """Получает информацио о пользователе в программе VK Testers

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.testersGetInfo',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkTestersGetInfo
        )

    async def experts_get_info_async(self, user_id: int, key: str = None, **kwargs) -> models.VkTestersGetInfo:
        """Получает информацио о пользователе в программе VK Experts

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.expertsGetInfo',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.VkTestersGetInfo
        )