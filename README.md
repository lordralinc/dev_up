# DEV UP API wrapper

![Version](https://img.shields.io/badge/version-1.0.1-blue)
![PyPI](https://img.shields.io/pypi/v/dev-up)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dev-up)
![GitHub](https://img.shields.io/github/license/lordralinc/idm_lp)


## Установка 
```shell
pip install -U https://github.com/lordralinc/dev_up/archive/master.zip
```


## Получение токена
[dev-up.ru](https://dev-up.ru/lk)

## Использование

```python
from dev_up import DevUpAPI

api = DevUpAPI("token")
profile = api.profile.get()
stickers = api.vk.get_stickers(1)
```

## Методы

| Секция  | Метод        | Параметры                    | Описание                                |
|---------|--------------|------------------------------|-----------------------------------------|
| vk      | get_stickers | user_id - VK ID пользователя | Получает список стикеров пользователя   |
| vk      | get_groups   | user_id - VK ID пользователя | Получает список групп пользователя      |
| vk      | get_apps     | user_id - VK ID пользователя | Получает список приложений пользователя |
| profile | get          |                              | Получает информацию о профиле           |
| audio   | speech       | url - ссылка на mp3          | Преобразование аудио в текст            |
