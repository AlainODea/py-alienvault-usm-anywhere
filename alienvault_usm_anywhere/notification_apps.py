"""
alienvault_usm_anywhere.notification_apps
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

    def list_targets(self):
        """List notification targets

        :return:
        """
        r = self.client.s.get(f"https://{self.client.domain}/api/2.0/apps/notification/targets")
        return raise_on_error(r).json()

    def create_target(self, notification_app, notification_target_name, notification_preferences, notification_type):
        """Create a notification target

        :param notification_app: amazon-sns, datadog, amazon-ses, pagerduty, or slack
        :param notification_target_name: UUID (client-generated?)
        :param notification_preferences: app-specific configuration string (may be JSON encoded as a string)
        :param notification_type: SNS, Datadog, SES, PagerDuty, or Slack
        :return:
        """
        r = self.client.s.post(f"https://{self.client.domain}/api/2.0/apps/notification/targets",
                               json={
                                   'notificationApp': notification_app,
                                   'notificationTargetName': notification_target_name,
                                   'notificationPreferences': notification_preferences,
                                   'notificationType': notification_type,
                               })
        return raise_on_error(r).json()
