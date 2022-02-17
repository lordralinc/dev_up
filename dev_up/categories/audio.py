import typing as ty

from dev_up import models
from dev_up.base.category import APICategory


class AudioAPICategory(APICategory):

    async def speech(
            self,
            url: str,
            *,
            access_token: ty.Optional[str] = None,
            raise_error: bool = None,
            raw_response: bool = None,
            use_cache: bool = None
    ) -> models.AudioSpeechResponse:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        :param access_token: токен
        :param raise_error: вызывать исключение `DevUpResponseException`
        :param raw_response: возвращать необработанный ответ
        :param use_cache: использовать кэш
        """
        return await self.api.make_request(
            method="audio.speech",
            data=dict(url=url),
            access_token=access_token,
            request_model=models.AudioSpeechRequest,
            response_model=models.AudioSpeechResponse,
            raise_error=raise_error,
            raw_response=raw_response,
            use_cache=use_cache
        )
