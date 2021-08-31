import typing as ty
from dev_up import models
from dev_up.categories.base import BaseAPICategories


class WarfaceAPICategories(BaseAPICategories):

    def get_info(
        self, 
        nick: str, 
        type: ty.Union[models.WarfaceGetInfoTypeEnum, str] = models.WarfaceGetInfoTypeEnum.STATISTICS, 
        key: str = None, 
        **kwargs
    ) -> models.WarfaceGetInfo:
        """Получает информацию об игроке Warface

        :param nick: Ник игрока
        :param type: Тип инфромации, defaults to models.WarfaceGetInfoTypeEnum.STATISTICS
        :param key: Ключ доступа, defaults to None
        :return: Информация об игроке. response зависит от переданного type
        """
        return self.api.make_request(
            method='warface.getInfo',
            data=dict(nick=nick, type=models.WarfaceGetInfoTypeEnum(type).value, key=key, **kwargs),
            dataclass=models.WarfaceGetInfo
        )


    async def get_info_async(
        self, 
        nick: str, 
        type: ty.Union[models.WarfaceGetInfoTypeEnum, str] = models.WarfaceGetInfoTypeEnum.STATISTICS, 
        key: str = None, 
        **kwargs
    ) -> models.WarfaceGetInfo:
        """Получает информацию об игроке Warface

        :param nick: Ник игрока
        :param type: Тип инфромации, defaults to models.WarfaceGetInfoTypeEnum.STATISTICS
        :param key: Ключ доступа, defaults to None
        :return: Информация об игроке. response зависит от переданного type
        """
        return await self.api.make_request_async(
            method='warface.getInfo',
            data=dict(nick=nick, type=models.WarfaceGetInfoTypeEnum(type).value, key=key, **kwargs),
            dataclass=models.WarfaceGetInfo
        )