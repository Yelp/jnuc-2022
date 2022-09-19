# OktaIDlib

## Intro

Small python script/library to pull application groups (AD Sync groups) from Okta's API.

## Config

The configuration is dead simple, you require only your domain and an API token. For security purposes, ensure  you are
using a token with limited access.

```yaml
---
token: verysecrettoken
okta_domain: yourdomain.okta.com
```

## Usage

Import the module and use accordingly.
