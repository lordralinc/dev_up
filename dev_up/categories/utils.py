from typing import Union

from dev_up import models
from dev_up.categories.base import BaseAPICategories


class UtilsAPICategories(BaseAPICategories):

    def md5_generate(self, text: str, key: str = None, **kwargs) -> models.UtilsMD5Generate:
        """Получить хэш md5 из текста

        :param text: текст
        :param key: Ключ доступа
        """
        return self.api.make_request(
            method='utils.md5Generate',
            data=dict(text=text, key=key, **kwargs),
            dataclass=models.UtilsMD5Generate
        )

    def get_server_time(self, key: str = None, **kwargs) -> models.UtilsGetServerTime:
        """Возвращает текущее время на сервере в unixtime (МСК)"""
        return self.api.make_request(
            method="utils.getServerTime",
            data=dict(key=key, **kwargs),
            dataclass=models.UtilsGetServerTime
        )

    def create_short_link(self, url: str, key: str = None, **kwargs) -> models.UtilsCreateShortLink:
        """Сокращение ссылок"""
        return self.api.make_request(
            method="utils.createShortLink",
            data=dict(url=url, key=key, **kwargs),
            dataclass=models.UtilsCreateShortLink
        )

    # noinspection PyArgumentList
    def notifications_links(
            self,
            code: str,
            status: Union[int, models.NotificationsLinksStatus],
            key: str = None,
            **kwargs
    ) -> models.UtilsNotificationsLinks:
        """Управление уведомлениями от ссылок"""
        return self.api.make_request(
            method="utils.notificationsLinks",
            data=dict(code=code, status=models.NotificationsLinksStatus(status).value, key=key, **kwargs),
            dataclass=models.UtilsNotificationsLinks
        )

    def get_web_info(self, address: str, key: str = None, **kwargs) -> models.UtilsGetWebInfo:
        """Информация о сервере"""
        return self.api.make_request(
            method="utils.getWebInfo",
            data=dict(address=address, key=key, **kwargs),
            dataclass=models.UtilsGetWebInfo
        )

    def number_identifier(self, number: str, key: str = None, **kwargs) -> models.UtilsNumberIdentifier:
        """Информация о номере телефона"""
        return self.api.make_request(
            method="utils.number_identifier",
            data=dict(number=number, key=key, **kwargs),
            dataclass=models.UtilsNumberIdentifier
        )

    def check_link(self, url: str, key: str = None, **kwargs) -> models.UtilsCheckLink:
        """Получает адрес, на который ведет сокращенная ссылка"""
        return self.api.make_request(
            method="utils.checkLink",
            data=dict(url=url, key=key, **kwargs),
            dataclass=models.UtilsCheckLink
        )


    async def md5_generate_async(self, text: str, key: str = None, **kwargs) -> models.UtilsMD5Generate:
        """Получить хэш md5 из текста

        :param text: текст
        :param key: Ключ доступа
        """
        return await self.api.make_request_async(
            method='utils.md5Generate',
            data=dict(text=text, key=key, **kwargs),
            dataclass=models.UtilsMD5Generate
        )

    async def get_server_time_async(self, key: str = None, **kwargs) -> models.UtilsGetServerTime:
        """Возвращает текущее время на сервере в unixtime (МСК)"""
        return await self.api.make_request_async(
            method="utils.getServerTime",
            data=dict(key=key, **kwargs),
            dataclass=models.UtilsGetServerTime
        )

    async def create_short_link_async(self, url: str, key: str = None, **kwargs) -> models.UtilsCreateShortLink:
        """Сокращение ссылок"""
        return await self.api.make_request_async(
            method="utils.createShortLink",
            data=dict(url=url, key=key, **kwargs),
            dataclass=models.UtilsCreateShortLink
        )

    # noinspection PyArgumentList
    async def notifications_links_async(
            self,
            code: str,
            status: Union[int, models.NotificationsLinksStatus],
            key: str = None,
            **kwargs
    ) -> models.UtilsNotificationsLinks:
        """Управление уведомлениями от ссылок"""
        return await self.api.make_request_async(
            method="utils.notificationsLinks",
            data=dict(code=code, status=models.NotificationsLinksStatus(status).value, key=key, **kwargs),
            dataclass=models.UtilsNotificationsLinks
        )

    async def get_web_info_async(self, address: str, key: str = None, **kwargs) -> models.UtilsGetWebInfo:
        """Информация о сервере"""
        return await self.api.make_request_async(
            method="utils.getWebInfo",
            data=dict(address=address, key=key, **kwargs),
            dataclass=models.UtilsGetWebInfo
        )

    async def number_identifier_async(self, number: str, key: str = None, **kwargs) -> models.UtilsNumberIdentifier:
        """Информация о номере телефона"""
        return await self.api.make_request_async(
            method="utils.number_identifier",
            data=dict(number=number, key=key, **kwargs),
            dataclass=models.UtilsNumberIdentifier
        )

    async def check_link_async(self, url: str, key: str = None, **kwargs) -> models.UtilsCheckLink:
        """Получает адрес, на который ведет сокращенная ссылка"""
        return await self.api.make_request_async(
            method="utils.checkLink",
            data=dict(url=url, key=key, **kwargs),
            dataclass=models.UtilsCheckLink
        )
