# DEV UP API wrapper

![PyPI](https://img.shields.io/pypi/v/dev-up)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dev-up)
![GitHub](https://img.shields.io/github/license/lordralinc/idm_lp)
[![Downloads](https://pepy.tech/badge/dev-up)](https://pepy.tech/project/dev-up)
## Установка 
```shell
pip install -U https://github.com/lordralinc/dev_up/archive/master.zip
```

или 

```shell
pip install dev_up
```



## Получение токена
[dev-up.ru](https://dev-up.ru/lk)

## Использование

```python
from dev_up import DevUpAPI

api = DevUpAPI("token")
profile = api.profile.get()
stickers = api.vk.get_stickers(1)

custom = api.make_request(
    "section.method", 
    data=dict(param1="foo", param2="bar"), 
    dataclass=dict
)
```

```python
# Использование с динамическим ключом доступа
from dev_up import DevUpAPI

api = DevUpAPI()
profile = await api.profile.get_async(key='token')
stickers = await api.vk.get_stickers_async(1, key='token')

custom = api.make_request(
    "section.method", 
    data=dict(param1="foo", param2="bar", key='token'), 
    dataclass=dict
)
```

```python
# Асинхронное использование
from dev_up import DevUpAPI

api = DevUpAPI("token")
profile = await api.profile.get_async()
stickers = await api.vk.get_stickers_async(1)

custom = await api.make_request_async(
    "section.method", 
    data=dict(param1="foo", param2="bar"), 
    dataclass=dict
)
```

## Методы

| Секция    | Метод                  | Параметры                                            | Описание                                                  |
|-----------|------------------------|------------------------------------------------------|-----------------------------------------------------------|
| vk        | get_stickers           | `user_id` - VK ID пользователя                       | Получает список стикеров пользователя                     |
| vk        | get_sticker_info       | `sticker_id` - ID стикера                            | Получает информацию о стикере и стикер-паке               |
| vk        | get_groups             | `user_id` - VK ID пользователя                       | Получает список групп пользователя                        |
| vk        | get_apps               | `user_id` - VK ID пользователя                       | Получает список приложений пользователя                   |
| vk        | search_playlists       | `q` - Поисковая строка                               | Получает список плейлистов                                |
| vk        | search_audio           | `q` - Поисковая строка                               | Получает список аудиозаписей                              |
| vk        | testers_get_info       | `user_id` - VK ID пользователя                       | Получает информацио о пользователе в программе VK Testers |
| vk        | experts_get_info       | `user_id` - VK ID пользователя                       | Получает информацио о пользователе в программе VK Experts |
| vk        | group_get_managers     | `group_id` - VK ID группы                            | Получает информацио об администраторах группы             |
| vk        | user_get_subscriptions | `user_id` - VK ID пользователя                       | Получает информацио об подписках польователя              |
| vk        | set_steps              | `access_token` - Токен VK Me                         | Устанавливает количество шагов                            |
| profile   | get                    | `user_id` - VK ID пользователя                       | Получает информацию о профиле                             |
| profile   | buy_premium            |                                                      | Получение premium статуса                                 |
| profile   | buy_limit              | `amount` - количество запросов                       | Покупка лимита                                            |
| profile   | get_balance_link       | `amount` - сумма<br>`vk` - VK ID пользователя        | Получение ссылки на пополнение баланса                    |
| profile   | set_key                |                                                      | Обнуление ключа доступа                                   |
| audio     | speech                 | `url` - ссылка на mp3                                | Преобразование аудио в текст                              |
| utils     | md5_generate           | `text` - текст                                       | Получить хэш md5 из текста                                |
| utils     | get_server_time        |                                                      | Возвращает текущее время на сервере в unixtime (МСК).     |
| utils     | get_short_link         | `url` - ссылка                                       | Сокращение ссылок                                         |
| utils     | notifications_links    | `code` - код ссылки<br>`status` - статус уведомлений | Управление уведомлениями от ссылок                        |
| utils     | get_web_info           | `address` - IP или URL                               | Информация о сервере                                      |
| utils     | number_identifier      | `number` - номер телефона                            | Информация о номере телефона                              |
| utils     | check_link             | `url` - ссылка                                       | Получает адрес, на который ведет сокращенная ссылка       |
| warface   | get_info               | `nick` - ник игрока, `type` - тип информации         | Получает информацию об игроке Warface                     |
