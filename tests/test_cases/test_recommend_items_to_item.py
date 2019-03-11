#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.item_to_item_recommendation import ItemToItemRecommendationTest
from recombee_api_client.api_requests import *

class RecommendItemsToItemTestCase (ItemToItemRecommendationTest):

    def create_request(self, item_id, target_user_id, count, filter=None, booster=None, cascade_create=None, scenario=None, logic=None, return_properties=None, included_properties=None, user_impact=None, diversity=None, min_relevance=None, rotation_rate=None, rotation_time=None, expert_settings=None, return_ab_group=None):
        return RecommendItemsToItem(item_id, target_user_id, count, filter=filter, booster=booster, cascade_create=cascade_create, scenario=scenario, logic=logic, return_properties=return_properties, included_properties=included_properties, user_impact=user_impact, diversity=diversity, min_relevance=min_relevance, rotation_rate=rotation_rate, rotation_time=rotation_time, expert_settings=expert_settings, return_ab_group=return_ab_group)
