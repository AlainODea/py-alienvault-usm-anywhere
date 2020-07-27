"""
alienvault_usm_anywhere
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

import requests
from getpass import getpass

from alienvault_usm_anywhere.correlation_lists import resource as correlation_lists
from alienvault_usm_anywhere.orchestration_rules import resource as orchestration_rules
from alienvault_usm_anywhere.notification_apps import resource as notification_apps
from alienvault_usm_anywhere.asset_groups import resource as asset_groups
from alienvault_usm_anywhere.scheduler import resource as scheduler
from alienvault_usm_anywhere.types import *


def client(domain):
    s = __create_session()

    __load_spa(domain, s)
    __do_login(domain, s)
    __do_mfa(domain, s)

    return Client(s, domain)


def __load_spa(domain, s):
    r = s.get(f"https://{domain}/")
    raise_on_error(r)
    s.headers.update({
        'X-XSRF-TOKEN': r.cookies['XSRF-TOKEN'],
        'Origin': f"https://{domain}",
        'Referer': f"https://{domain}/",
    })
    return r


def __do_login(domain, s):
    r = s.post(
        f"https://{domain}/api/2.0/login",
        json={
            "email": input(f"Username ({domain}): "),
            "password": getpass(f"Password ({domain}): "),
        }
    )
    return raise_on_error(r)


def __do_mfa(domain, s):
    r = s.post(
        f"https://{domain}/api/2.0/verify",
        json={
            "token": getpass(f"OTP/MFA token ({domain}): "),
        }
    )
    return raise_on_error(r)


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
