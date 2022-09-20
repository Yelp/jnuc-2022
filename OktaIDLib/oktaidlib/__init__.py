#!/usr/bin/env ptyhon3
# -*- coding: utf-8 -*-

from urllib.parse import urlencode
import requests
import json
import yaml


class OktaIDLib:
    def __init__(self, config_file=None):
        if not config_file:
            config_file = "/usr/local/munki/okta_config.yaml"

        with open(config_file, "r") as file:
            # Open file stream and attempt to load YAML
            config = yaml.load(file, Loader=yaml.SafeLoader)

        okta_domain = config.get("okta_domain")
        self._api_token = config.get("token")
        self._base_url = f"https://{okta_domain}"
        self._default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self._default_headers["Authorization"] = "SSWS " f"{self._api_token}"

    def _execute_request(self, api_url):
        response = requests.request(
            "GET", api_url, headers=self._default_headers, data={}
        )

        return json.loads(response.text)

    def get_user(self, user_name):
        encoded_query = urlencode({"search": f'profile.login eq "{user_name}"'})
        api_url = f"{self._base_url}/api/v1/users"
        api_url += f"/?{encoded_query}"

        found_users = self._execute_request(api_url)

        return found_users[0]

    def get_ad_groups(self, user_id):
        api_url = f"{self._base_url}/api/v1/users"
        api_url += f"/{user_id}/groups"
        groups = self._execute_request(api_url)

        return [
            g["profile"]["dn"]
            for g in groups
            if g["type"] == "APP_GROUP" and g["profile"].get("dn") is not None
        ]
