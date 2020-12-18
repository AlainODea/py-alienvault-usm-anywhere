"""
alienvault_usm_anywhere.types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

from requests_toolbelt.utils import dump


class Client:
    def __init__(self, s, domain):
        self.s = s
        self.domain = domain

class AuthException(Exception):
    """Exception raised for AlienVault authentication errors """
    def __init__(self, r, message):
        self.r = r
        self.message = message

class ClientException(Exception):
    """Exception raised for AlienVault client errors """
    def __init__(self, r, message):
        self.r = r
        self.message = message


def dump_all(r):
    data = dump.dump_all(r)
    print(data.decode('utf-8'))


def raise_on_error(r):
    if r.status_code == 401:
        raise AuthException(r, f"{r.status_code}: {r.content.decode('utf-8', 'strict')}")
    elif r.status_code != 200:
        raise ClientException(r, f"{r.status_code}: {r.content.decode('utf-8', 'strict')}")
    return r
