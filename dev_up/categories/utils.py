import typing as ty

from dev_up import models
from dev_up.base.category import APICategory


class UtilsAPICategory(APICategory):

    async def check_link(
            self,
            url: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.UtilsCheckLinkResponse:
        """Получает адрес, на который ведет сокращенная ссылка

        :param url: проверяемая ссылка
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="utils.checkLink",
            data=dict(url=url),
            access_token=access_token,
            request_model=models.UtilsCheckLinkRequest,
            response_model=models.UtilsCheckLinkResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def create_short_link(
            self,
            url: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.UtilsCreateShortLinkResponse:
        """Сокращение ссылок

        :param url: ссылка
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="utils.createShortLink",
            data=dict(url=url),
            access_token=access_token,
            request_model=models.UtilsCreateShortLinkRequest,
            response_model=models.UtilsCreateShortLinkResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get_server_time(
            self,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.UtilsGetServerTimeResponse:
        """Возвращает текущее время на сервере

        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="utils.getServerTime",
            data=dict(),
            access_token=access_token,
            request_model=models.UtilsGetServerTimeRequest,
            response_model=models.UtilsGetServerTimeResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get_web_info(
            self,
            address: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.UtilsGetWebInfoResponse:
        """Информация о сервере

        :param address: URL или IP сервера
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="utils.getWebInfo",
            data=dict(address=address),
            access_token=access_token,
            request_model=models.UtilsGetWebInfoRequest,
            response_model=models.UtilsGetWebInfoResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def md5_generate(
            self,
            text: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.UtilsMD5GenerateResponse:
        """Получить хэш md5 от текста

        :param text: значение от которого необходимо получить хэш
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="utils.md5Generate",
            data=dict(text=text),
            access_token=access_token,
            request_model=models.UtilsMD5GenerateRequest,
            response_model=models.UtilsMD5GenerateResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def notifications_links(
            self,
            code: str,
            status: models.UtilsNotificationsLinksStatus,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.UtilsNotificationsLinksResponse:
        """Получить хэш md5 от текста

        :param code: код ссылки
        :param status: статус оповещений
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="utils.notificationsLinks",
            data=dict(code=code, status=status),
            access_token=access_token,
            request_model=models.UtilsNotificationsLinksRequest,
            response_model=models.UtilsNotificationsLinksResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )
