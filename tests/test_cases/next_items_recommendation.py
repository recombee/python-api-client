#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class NextItemsRecommendationTest(RecommendationsTest):

    def create_request(self,recomm_id,count):
        pass

    def test_next_items_recommendation(self):

        # it 'recommends'
        req = RecommendItemsToUser('entity_id', 3, return_properties=True)
        resp = self.client.send(req)
        req = self.create_request(resp['recommId'], 3)
        resp = self.client.send(req)
        self.assertEqual(len(resp['recomms']), 3)
        req = self.create_request(resp['recommId'], 3)
        resp = self.client.send(req)
        self.assertEqual(len(resp['recomms']), 3)

