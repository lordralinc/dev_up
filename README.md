# DEV UP API wrapper

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![GitHub](https://img.shields.io/github/license/lordralinc/idm_lp)

## Install 
```shell
pip install -U https://github.com/lordralinc/dev_up/archive/master.zip
```

## Usage

```python
from dev_up import DevUpAPI

api = DevUpAPI("token")
profile = api.profile.get()
```