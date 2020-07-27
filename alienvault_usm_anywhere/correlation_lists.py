"""
alienvault_usm_anywhere.correlation_lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

from alienvault_usm_anywhere.types import *


def resource(client):
    return Resource(client)


class Resource:
    def __init__(self, client):
        self.client = client

    def search(self, page=0, query='', size=20, sort='name,asc'):
        """Search for matching correlation lists

        :param page: specifies the page number (zero based) of results to return
        :param query: words to find in the list names
        :param size: number of results per page
        :param sort: field name to sort by and whether to sort ascending or decending (ex: 'name,asc')
        :return:
        """
        r = self.client.s.get(f"https://{self.client.domain}/api/2.0/correlationLists/search/r",
                              params={
                                  'page': page,
                                  'query': query,
                                  'size': size,
                                  'sort': sort,
                              })
        return raise_on_error(r).json()

    def list_items(self, list_id, page=0, size=20, sort='val,asc'):
        """List items of a correlation list

        :param list_id:
        :param page: specifies the page number (zero based) of results to return.
        :param size:
        :param sort: field name to sort by and whether to sort ascending or decending (ex: 'val,asc')
        :return:
        """
        r = self.client.s.get(f"https://{self.client.domain}/api/2.0/correlationLists/{list_id}/items",
                              params={
                                  'page': page,
                                  'size': size,
                                  'sort': sort,
                              })
        return raise_on_error(r).json()

    def create(self, name, description=''):
        """Create a correlation list

        :param name: name of the correlation list to create. Only alphanumeric allowed (no spaces or hyphens)
        :param description: description of the list
        :return: correlation list that was created
        """
        r = self.client.s.post(f"https://{self.client.domain}/api/2.0/correlationLists",
                               json={
                                   'name': name,
                                   'description': description,
                               })
        return raise_on_error(r).json()

    def create_item(self, list_id, val):
        """Add an item to a correlation list

        :param list_id:
        :param val: new value for the item
        :return: correlation list item that was created
        """
        r = self.client.s.post(f"https://{self.client.domain}/api/2.0/correlationLists/{list_id}/items",
                               json={
                                   'id': None,
                                   'val': str(val),
                               })
        return raise_on_error(r).json()

    def update_item(self, list_id, item_id, val):
        """Add an item to a correlation list

        :param list_id: ID of the list which contains the item to update
        :param item_id: ID of the item to update
        :param val: new value for the item
        :return:
        """
        r = self.client.s.put(f"https://{self.client.domain}/api/2.0/correlationLists/{list_id}/items",
                              json={
                                  'id': item_id,
                                  'val': str(val),
                              })
        return raise_on_error(r).json()
