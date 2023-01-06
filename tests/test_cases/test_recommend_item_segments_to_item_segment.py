#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommend_item_segments_to_item_segment import RecommendItemSegmentsToItemSegmentTest
from recombee_api_client.api_requests import *

class RecommendItemSegmentsToItemSegmentTestCase(RecommendItemSegmentsToItemSegmentTest):

    def create_request(self, context_segment_id, target_user_id, count, scenario=None, cascade_create=None, filter=None, booster=None, logic=None, expert_settings=None, return_ab_group=None):
        return RecommendItemSegmentsToItemSegment(context_segment_id, target_user_id, count, scenario=scenario, cascade_create=cascade_create, filter=filter, booster=booster, logic=logic, expert_settings=expert_settings, return_ab_group=return_ab_group)
