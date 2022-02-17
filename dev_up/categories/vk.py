import typing
import typing as ty

from dev_up import models
from dev_up.base.category import APICategory


class VKAPICategory(APICategory):

    async def experts_get_info(
            self,
            user_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKExpertsGetInfoResponse:
        """Получает информацио о пользователе в программе VK Experts

        :param user_id: VK ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.expertsGetInfo",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.VKExpertsGetInfoRequest,
            response_model=models.VKExpertsGetInfoResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get_apps(
            self,
            user_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKGetAppsResponse:
        """Получает список приложений пользователя

        :param user_id: VK ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.getApps",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.VKExpertsGetInfoRequest,
            response_model=models.VKGetAppsResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get_groups(
            self,
            user_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKGetGroupsResponse:
        """Получает список групп пользователя

        :param user_id: VK ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.getGroups",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.VKGetGroupsRequest,
            response_model=models.VKGetGroupsResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get_sticker_info(
            self,
            sticker_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKGetStickerInfoResponse:
        """Получает информацию о стикере и стикер-паке

        :param sticker_id: ID стикера
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.getStickerInfo",
            data=dict(sticker_id=sticker_id),
            access_token=access_token,
            request_model=models.VKGetStickerInfoRequest,
            response_model=models.VKGetStickerInfoResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get_stickers(
            self,
            user_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKGetStickersResponse:
        """Получает список стикеров пользователя

        :param user_id: VK ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.getStickers",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.VKGetStickersRequest,
            response_model=models.VKGetStickersResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def group_get_managers(
            self,
            group_id: typing.Union[str, int],
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKGroupGetManagersResponse:
        """Получает информацию об администраторах группы

        :param group_id: VK ID группы
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.groupGetManagers",
            data=dict(group_id=group_id),
            access_token=access_token,
            request_model=models.VKGroupGetManagersRequest,
            response_model=models.VKGroupGetManagersResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def search_audio(
            self,
            q: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKSearchAudioResponse:
        """Поиск аудиозаписей

        :param q: поисковая строка
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.searchAudio",
            data=dict(q=q),
            access_token=access_token,
            request_model=models.VKSearchAudioRequest,
            response_model=models.VKSearchAudioResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def search_playlists(
            self,
            q: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKSearchPlaylistsResponse:
        """Поиск плейлистов

        :param q: поисковая строка
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.searchPlaylists",
            data=dict(q=q),
            access_token=access_token,
            request_model=models.VKSearchPlaylistsRequest,
            response_model=models.VKSearchPlaylistsResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def set_steps(
            self,
            vk_me_access_token: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKSetStepsResponse:
        """Устанавливает количество шагов

        :param vk_me_access_token: токен приложения VK ME
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.setSteps",
            data=dict(access_token=vk_me_access_token),
            access_token=access_token,
            request_model=models.VKSetStepsRequest,
            response_model=models.VKSetStepsResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def testers_get_info(
            self,
            user_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKSearchPlaylistsResponse:
        """Получает информацию о пользователе в программе VK Testers

        :param user_id: VK ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.testersGetInfo",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.VKSearchPlaylistsRequest,
            response_model=models.VKSearchPlaylistsResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def user_get_subscriptions(
            self,
            user_id: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.VKUserGetSubscriptionsResponse:
        """Получает информацию об подписках пользователя

        :param user_id: VK ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="vk.userGetSubscriptions",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.VKUserGetSubscriptionsRequest,
            response_model=models.VKUserGetSubscriptionsResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )
