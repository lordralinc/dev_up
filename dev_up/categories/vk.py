from dev_up import models
from dev_up.categories.base import BaseAPICategories


class VkAPICategories(BaseAPICategories):

    def get_stickers(self, user_id: int, key: str = None) -> models.VkGetStickers:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getStickers',
            data=dict(user_id=user_id, key=key),
            dataclass=models.VkGetStickers
        )

    def get_sticker_info(self, sticker_id: int, key: str = None) -> models.VkGetStickerInfo:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getStickerInfo',
            data=dict(sticker_id=sticker_id, key=key),
            dataclass=models.VkGetStickerInfo
        )

    def get_groups(self, user_id: int, key: str = None) -> models.VkGetGroups:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getGroups',
            data=dict(user_id=user_id, key=key),
            dataclass=models.VkGetGroups
        )

    def get_apps(self, user_id: int, key: str = None) -> models.VkGetApps:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='vk.getApps',
            data=dict(user_id=user_id, key=key),
            dataclass=models.VkGetApps
        )

    async def get_stickers_async(self, user_id: int, key: str = None) -> models.VkGetStickers:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getStickers',
            data=dict(user_id=user_id, key=key),
            dataclass=models.VkGetStickers
        )

    async def get_sticker_info_async(self, sticker_id: int, key: str = None) -> models.VkGetStickerInfo:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getStickerInfo',
            data=dict(sticker_id=sticker_id, key=key),
            dataclass=models.VkGetStickerInfo
        )

    async def get_groups_async(self, user_id: int, key: str = None) -> models.VkGetGroups:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getGroups',
            data=dict(user_id=user_id, key=key),
            dataclass=models.VkGetGroups
        )

    async def get_apps_async(self, user_id: int, key: str = None) -> models.VkGetApps:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='vk.getApps',
            data=dict(user_id=user_id, key=key),
            dataclass=models.VkGetApps
        )
