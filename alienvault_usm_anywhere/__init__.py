"""
alienvault_usm_anywhere
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

import requests
import browser_cookie3

from alienvault_usm_anywhere.correlation_lists import resource as correlation_lists
from alienvault_usm_anywhere.orchestration_rules import resource as orchestration_rules
from alienvault_usm_anywhere.notification_apps import resource as notification_apps
from alienvault_usm_anywhere.asset_groups import resource as asset_groups
from alienvault_usm_anywhere.scheduler import resource as scheduler
from alienvault_usm_anywhere.types import *

def client(domain, auth_cookies):
    s = __create_session()
    s.cookies.update(auth_cookies)

    return Client(s, domain)

def get_auth_cookies(domain, browser):
    auth_cookies = {}

    if browser == "firefox":
        cookie_jar = browser_cookie3.firefox()
    elif browser == "chrome":
        cookie_jar = browser_cookie3.chrome()
    else:
        raise ValueError("Argument \"browser\" must be one of \"chrome\" or \"firefox\"")

    for cookie in cookie_jar:
        if cookie.domain == domain and cookie.name in ("XSRF-TOKEN", "JSESSIONID"):
            auth_cookies.update({cookie.name : cookie.value})
    return auth_cookies

def __create_session():
    s = requests.Session()
    headers_masquerade_firefox = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    s.headers.update(headers_masquerade_firefox)
    return s
