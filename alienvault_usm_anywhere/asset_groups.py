"""
alienvault_usm_anywhere.asset_groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

from alienvault_usm_anywhere.types import *


def resource(client):
    return Resource(client)


class Resource:
    def __init__(self, client):
        self.client = client

    def search(self, page=0, query='', size=20, sort='created,desc'):
        """Search for matching asset groups

        :param page: specifies the page number (zero based) of results to return
        :param query: words to find in the list names
        :param size: number of results per page
        :param sort: field name to sort by and whether to sort ascending or decending (ex: 'created,desc')
        :return:
        """
        r = self.client.s.get(f"https://{self.client.domain}/api/2.0/assetGroups/search/r",
                              params={
                                  'page': page,
                                  'query': query,
                                  'size': size,
                                  'sort': sort,
                              })
        return raise_on_error(r).json()
