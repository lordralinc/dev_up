import typing as ty

from dev_up import models
from dev_up.base.category import APICategory


class ProfileAPICategory(APICategory):

    async def buy_limit(
            self,
            amount: int,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.ProfileBuyLimitResponse:
        """Покупка лимита

        :param amount: количество
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="profile.buyLimit",
            data=dict(amount=amount),
            access_token=access_token,
            request_model=models.ProfileBuyLimitRequest,
            response_model=models.ProfileBuyLimitResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def buy_premium(
            self,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.ProfileBuyPremiumResponse:
        """Покупка premium статуса

        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="profile.buyPremium",
            data=dict(),
            access_token=access_token,
            request_model=models.ProfileBuyPremiumRequest,
            response_model=models.ProfileBuyPremiumResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )

    async def get(
            self,
            user_id: int = None,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.ProfileGetResponse:
        """Получает информацию о профиле DEV-UP

        :param user_id: ID пользователя
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="profile.get",
            data=dict(user_id=user_id),
            access_token=access_token,
            request_model=models.ProfileGetRequest,
            response_model=models.ProfileGetResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )
