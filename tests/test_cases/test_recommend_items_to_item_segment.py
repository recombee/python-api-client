#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommend_to_item_segment import RecommendToItemSegmentTest
from recombee_api_client.api_requests import *

class RecommendItemsToItemSegmentTestCase(RecommendToItemSegmentTest):

    def create_request(self, context_segment_id, target_user_id, count, scenario=None, cascade_create=None, return_properties=None, included_properties=None, filter=None, booster=None, logic=None, min_relevance=None, rotation_rate=None, rotation_time=None, expert_settings=None, return_ab_group=None):
        return RecommendItemsToItemSegment(context_segment_id, target_user_id, count, scenario=scenario, cascade_create=cascade_create, return_properties=return_properties, included_properties=included_properties, filter=filter, booster=booster, logic=logic, min_relevance=min_relevance, rotation_rate=rotation_rate, rotation_time=rotation_time, expert_settings=expert_settings, return_ab_group=return_ab_group)
