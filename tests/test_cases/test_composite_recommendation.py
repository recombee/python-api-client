#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.composite_recommendation import CompositeRecommendationTest
from recombee_api_client.api_requests.composite_recommendation import (
    CompositeRecommendation,
    DEFAULT,
)


class CompositeRecommendationTestCase(CompositeRecommendationTest):

    def create_request(
        self,
        scenario,
        count,
        item_id=DEFAULT,
        user_id=DEFAULT,
        logic=DEFAULT,
        segment_id=DEFAULT,
        cascade_create=DEFAULT,
        source_settings=DEFAULT,
        result_settings=DEFAULT,
        expert_settings=DEFAULT,
    ):
        return CompositeRecommendation(
            scenario,
            count,
            item_id=item_id,
            user_id=user_id,
            logic=logic,
            segment_id=segment_id,
            cascade_create=cascade_create,
            source_settings=source_settings,
            result_settings=result_settings,
            expert_settings=expert_settings,
        )
