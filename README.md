# DEV UP API wrapper

![PyPI](https://img.shields.io/pypi/v/dev-up)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dev-up)
![GitHub](https://img.shields.io/github/license/lordralinc/dev_up)
[![Downloads](https://pepy.tech/badge/dev-up)](https://pepy.tech/project/dev-up)
## Установка 
```shell
pip install dev_up
```



## Получение токена
[dev-up.ru](https://dev-up.ru/lk)

## Использование

```python
from dev_up import DevUpAPI

api = DevUpAPI("token")
profile = await api.profile.get()
stickers = await api.vk.get_stickers(1)

custom = await api.make_request(
    "section.method",
    data=dict(param1="foo", param2="bar")
)
```