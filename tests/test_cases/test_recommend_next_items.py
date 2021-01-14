#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.next_items_recommendation import NextItemsRecommendationTest
from recombee_api_client.api_requests import *

class RecommendNextItemsTestCase (NextItemsRecommendationTest):

    def create_request(self, recomm_id, count):
        return RecommendNextItems(recomm_id, count)
