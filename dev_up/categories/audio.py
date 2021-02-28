from dev_up import models
from dev_up.categories.base import BaseAPICategories


class AudioAPICategories(BaseAPICategories):

    def speech(self, url: str, key: str = None) -> models.AudioSpeech:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        :param key: токен
        """
        return self.api.make_request(
            method='audio.speech',
            data=dict(url=url, key=key),
            dataclass=models.AudioSpeech
        )

    async def speech_async(self, url: str, key: str = None) -> models.AudioSpeech:
        """Преобразование аудио в текст

        :param url: ссылка на mp3
        :param key: токен
        """
        return await self.api.make_request_async(
            method='audio.speech',
            data=dict(url=url, key=key),
            dataclass=models.AudioSpeech
        )
