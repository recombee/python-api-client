#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.item_to_item_recommendation import ItemToItemRecommendationTest
from recombee_api_client.api_requests import *

class RecommendItemsToItemTestCase (ItemToItemRecommendationTest):

    def create_request(self, item_id, target_user_id, count, scenario=None, cascade_create=None, return_properties=None, included_properties=None, filter=None, booster=None, logic=None, user_impact=None, diversity=None, min_relevance=None, rotation_rate=None, rotation_time=None, expert_settings=None, return_ab_group=None):
        return RecommendItemsToItem(item_id, target_user_id, count, scenario=scenario, cascade_create=cascade_create, return_properties=return_properties, included_properties=included_properties, filter=filter, booster=booster, logic=logic, user_impact=user_impact, diversity=diversity, min_relevance=min_relevance, rotation_rate=rotation_rate, rotation_time=rotation_time, expert_settings=expert_settings, return_ab_group=return_ab_group)
