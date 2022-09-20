# oktaidlib

## Intro

Small python script/library to pull application groups (AD Sync groups) from
Okta's API.

## Config

The configuration is dead simple, you require only your domain and an API token.
For security purposes, ensure you are using a token with limited access.

```yaml
---
# /usr/local/munki/okta_config.yaml
token: verysecrettoken
okta_domain: yourdomain.okta.com
```

## Usage

Import the module and use accordingly.

```python
from oktaidlib import OktaIDLib
from pprint import pprint

okta_config_path = '/usr/local/munki/okta_config.yaml'
okta = OktaIDLib(okta_config_path)
user = okta.get_user(user)
pprint(user)
```
