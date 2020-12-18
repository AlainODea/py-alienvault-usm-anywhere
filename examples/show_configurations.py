"""
show_configurations
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2020 by Alain O'Dea.
:license: Apache 2.0, see LICENSE for more details.
"""

import json
import alienvault_usm_anywhere
import sys


def main():
    subdomain = sys.argv[1]
    domain = "alienvault.cloud"

    auth_cookies = alienvault_usm_anywhere.get_auth_cookies(f"{subdomain}.{domain}", "firefox")
    api_client = alienvault_usm_anywhere.client(f"{subdomain}.{domain}", auth_cookies)

    correlation_lists = alienvault_usm_anywhere.correlation_lists(api_client)
    asset_groups = alienvault_usm_anywhere.asset_groups(api_client)
    orchestration_rules = alienvault_usm_anywhere.orchestration_rules(api_client)
    scheduler = alienvault_usm_anywhere.scheduler(api_client)

    print('========================================================================')
    print(f'Correlation lists ({api_client.domain}):')
    print('========================================================================')
    for correlation_list in correlation_lists.search()['_embedded']['correlationLists']:
        print(json.dumps(correlation_list, indent=2))
        correlation_list_items = correlation_lists.list_items(correlation_list['id'])
        for correlation_list_item in correlation_list_items['_embedded']['correlationListItems']:
            print(json.dumps(correlation_list_item, indent=2))

    print('========================================================================')
    print(f'Asset groups ({api_client.domain}):')
    print('========================================================================')
    for asset_group in asset_groups.search()['_embedded']['assetGroups']:
        print(json.dumps(asset_group, indent=2))

    print('========================================================================')
    print(f'Orchestration rules ({api_client.domain}):')
    print('========================================================================')
    for orchestration_rule in orchestration_rules.list()['_embedded']['orchestrationRules']:
        print(json.dumps(orchestration_rule, indent=2))

    print('========================================================================')
    print(f'Scheduler jobs ({api_client.domain}):')
    print('========================================================================')
    for scheduler_job in scheduler.list_jobs():
        print(json.dumps(scheduler_job, indent=2))


if __name__ == "__main__":
    main()
