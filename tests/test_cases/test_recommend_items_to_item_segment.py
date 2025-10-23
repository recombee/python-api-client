#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommend_to_item_segment import RecommendToItemSegmentTest
from recombee_api_client.api_requests.recommend_items_to_item_segment import (
    RecommendItemsToItemSegment,
    DEFAULT,
)


class RecommendItemsToItemSegmentTestCase(RecommendToItemSegmentTest):

    def create_request(
        self,
        context_segment_id,
        target_user_id,
        count,
        scenario=DEFAULT,
        cascade_create=DEFAULT,
        return_properties=DEFAULT,
        included_properties=DEFAULT,
        filter=DEFAULT,
        booster=DEFAULT,
        logic=DEFAULT,
        reql_expressions=DEFAULT,
        min_relevance=DEFAULT,
        rotation_rate=DEFAULT,
        rotation_time=DEFAULT,
        expert_settings=DEFAULT,
        return_ab_group=DEFAULT,
    ):
        return RecommendItemsToItemSegment(
            context_segment_id,
            target_user_id,
            count,
            scenario=scenario,
            cascade_create=cascade_create,
            return_properties=return_properties,
            included_properties=included_properties,
            filter=filter,
            booster=booster,
            logic=logic,
            reql_expressions=reql_expressions,
            min_relevance=min_relevance,
            rotation_rate=rotation_rate,
            rotation_time=rotation_time,
            expert_settings=expert_settings,
            return_ab_group=return_ab_group,
        )
