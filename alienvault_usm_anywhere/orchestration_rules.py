"""
alienvault_usm_anywhere.orchestration_rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

from alienvault_usm_anywhere.types import *


def resource(client):
    return Resource(client)


class Resource:
    def __init__(self, client):
        self.client = client

    def list(self):
        """List orchestration rules

        :return:
        """
        r = self.client.s.get(f"https://{self.client.domain}/api/2.0/orchestrationRules")
        return raise_on_error(r).json()

    def create(self, name, action, action_parameters, match_rule, ui_info, occurrences=1, length='1s'):
        """Create an orchestration rule (default enabled)

        :param name: name of the orchestration rule
        :param action: type of rule (suppression, drop (filtering), alarm, notification, or )
        :param action_parameters: parameters for the action (not used for suppression or drop (filtering) actions)
        :param match_rule: rule that matches events to trigger on
        :param ui_info: metadata for UI for interactively editing rule
        :param occurrences: number of occurrences to trigger on
        :param length: time period in which to accumulate occurrences
        :return:
        """
        r = self.client.s.post(f"https://{self.client.domain}/api/2.0/orchestrationRules",
                               json={
                                   'name': name,
                                   'action': action,
                                   'matchRule': match_rule,
                                   'occurrences': occurrences,
                                   'length': length,
                                   'uiInfo': ui_info,
                                   'actionParameters': action_parameters,
                               })
        return raise_on_error(r).json()

    def disable(self, rule_id):
        """Disable an orchestration rule

        :param rule_id: ID of the orchestration rule to disable
        :return:
        """
        r = self.client.s.delete(f"https://{self.client.domain}/api/2.0/orchestrationRules/{rule_id}/disable")
        return raise_on_error(r).json()

    def enable(self, rule_id):
        """Enable an orchestration rule

        :param rule_id: ID of the orchestration rule to disable
        :return:
        """
        r = self.client.s.out(f"https://{self.client.domain}/api/2.0/orchestrationRules/{rule_id}/enable")
        return raise_on_error(r).json()

    def update(self, rule_id, name, action, action_parameters, match_rule, ui_info, occurrences=1, length='1s'):
        """Update an orchestration rule

        :param rule_id: ID of the rule to update
        :param name: name of the orchestration rule
        :param action: type of rule (suppression, drop (filtering), alarm, notification, or )
        :param action_parameters: parameters for the action (not used for suppression or drop (filtering) actions)
        :param match_rule: rule that matches events to trigger on
        :param ui_info: metadata for UI for interactively editing rule
        :param occurrences: number of occurrences to trigger on
        :param length: time period in which to accumulate occurrences
        :return:
        """
        r = self.client.s.put(f"https://{self.client.domain}/api/2.0/orchestrationRules/{rule_id}",
                              json={
                                  'name': name,
                                  'action': action,
                                  'matchRule': match_rule,
                                  'occurrences': occurrences,
                                  'length': length,
                                  'uiInfo': ui_info,
                                  'actionParameters': action_parameters,
                              })
        return raise_on_error(r).json()
