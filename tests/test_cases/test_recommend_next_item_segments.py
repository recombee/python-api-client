#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.next_item_segments_recommendation import (
    NextItemSegmentsRecommendationTest,
)
from recombee_api_client.api_requests.recommend_next_item_segments import (
    RecommendNextItemSegments,
    DEFAULT,
)


class RecommendNextItemSegmentsTestCase(NextItemSegmentsRecommendationTest):

    def create_request(self, recomm_id, count):
        return RecommendNextItemSegments(recomm_id, count)
