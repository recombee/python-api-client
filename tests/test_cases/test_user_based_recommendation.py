#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommendation import RecommendationTest
from recombee_api_client.api_requests import *

class UserBasedRecommendationTestCase (RecommendationTest):

    def create_request(self, user_id, count, filter=None, booster=None, allow_nonexistent=None, cascade_create=None, scenario=None, return_properties=None, included_properties=None, diversity=None, min_relevance=None, rotation_rate=None, rotation_time=None):
        return UserBasedRecommendation(user_id, count, filter=filter, booster=booster, allow_nonexistent=allow_nonexistent, cascade_create=cascade_create, scenario=scenario, return_properties=return_properties, included_properties=included_properties, diversity=diversity, min_relevance=min_relevance, rotation_rate=rotation_rate, rotation_time=rotation_time)
