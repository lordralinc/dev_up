from dev_up import models
from dev_up.categories.base import BaseAPICategories


class ProfileAPICategories(BaseAPICategories):

    def get(self, key: str = None) -> models.ProfileGet:
        """Получает информацию о профиле DEV-UP"""
        return self.api.make_request(
            method='profile.get',
            data=dict(key=key),
            dataclass=models.ProfileGet
        )

    def balance_buy_premium(self, key: str = None) -> models.ProfileBalanceBuyPremium:
        """Получение premium статуса"""
        return self.api.make_request(
            method='profile.balanceBuyPremium',
            data=dict(key=key),
            dataclass=models.ProfileBalanceBuyPremium
        )

    def limit_buy(self, amount: int, key: str = None) -> models.ProfileLimitBuy:
        """Покупка лимита"""
        return self.api.make_request(
            method='profile.LimitBuy',
            data=dict(amount=amount, key=key),
            dataclass=models.ProfileLimitBuy
        )

    async def get_async(self, key: str = None) -> models.ProfileGet:
        """Получает информацию о профиле DEV-UP"""
        return await self.api.make_request_async(
            method='profile.get',
            data=dict(key=key),
            dataclass=models.ProfileGet
        )

    async def balance_buy_premium_async(self, key: str = None) -> models.ProfileBalanceBuyPremium:
        """Получение premium статуса"""
        return await self.api.make_request_async(
            method='profile.balanceBuyPremium',
            data=dict(key=key),
            dataclass=models.ProfileBalanceBuyPremium
        )

    async def limit_buy_async(self, amount: int, key: str = None) -> models.ProfileLimitBuy:
        """Покупка лимита"""
        return await self.api.make_request_async(
            method='profile.LimitBuy',
            data=dict(amount=amount, key=key),
            dataclass=models.ProfileLimitBuy
        )
