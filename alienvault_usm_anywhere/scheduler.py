"""
alienvault_usm_anywhere.scheduler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

from alienvault_usm_anywhere.types import *


def resource(client):
    return Resource(client)


class Resource:
    def __init__(self, client):
        self.client = client

    def list_jobs(self):
        """Search for matching asset groups

        :return:
        """
        r = self.client.s.get(f"https://{self.client.domain}/api/2.0/scheduler")
        return raise_on_error(r).json()
