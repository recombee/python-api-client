#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommend_to_item_segment import RecommendToItemSegmentTest
from recombee_api_client.api_requests.recommend_item_segments_to_item_segment import (
    RecommendItemSegmentsToItemSegment,
    DEFAULT,
)


class RecommendItemSegmentsToItemSegmentTestCase(RecommendToItemSegmentTest):

    def create_request(
        self,
        context_segment_id,
        target_user_id,
        count,
        scenario=DEFAULT,
        cascade_create=DEFAULT,
        filter=DEFAULT,
        booster=DEFAULT,
        logic=DEFAULT,
        expert_settings=DEFAULT,
        return_ab_group=DEFAULT,
    ):
        return RecommendItemSegmentsToItemSegment(
            context_segment_id,
            target_user_id,
            count,
            scenario=scenario,
            cascade_create=cascade_create,
            filter=filter,
            booster=booster,
            logic=logic,
            expert_settings=expert_settings,
            return_ab_group=return_ab_group,
        )
