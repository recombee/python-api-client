#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommendation import RecommendationTest
from recombee_api_client.api_requests import *

class RecommendUsersToItemTestCase (RecommendationTest):

    def create_request(self, item_id, count, scenario=None, cascade_create=None, return_properties=None, included_properties=None, filter=None, booster=None, logic=None, diversity=None, expert_settings=None, return_ab_group=None):
        return RecommendUsersToItem(item_id, count, scenario=scenario, cascade_create=cascade_create, return_properties=return_properties, included_properties=included_properties, filter=filter, booster=booster, logic=logic, diversity=diversity, expert_settings=expert_settings, return_ab_group=return_ab_group)
