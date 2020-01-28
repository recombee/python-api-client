#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.search import SearchTest
from recombee_api_client.api_requests import *

class SearchItemsTestCase (SearchTest):

    def create_request(self, user_id, search_query, count, scenario=None, cascade_create=None, return_properties=None, included_properties=None, filter=None, booster=None, logic=None, expert_settings=None, return_ab_group=None):
        return SearchItems(user_id, search_query, count, scenario=scenario, cascade_create=cascade_create, return_properties=return_properties, included_properties=included_properties, filter=filter, booster=booster, logic=logic, expert_settings=expert_settings, return_ab_group=return_ab_group)
