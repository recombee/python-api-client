#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

import time
from abc import ABC, abstractmethod
from tests.test_cases.recombee_test import (
    RecombeeTest,
    InteractionsTest,
    RecommendationsTest,
)
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *


class NextItemSegmentsRecommendationTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self, recomm_id, count):
        pass

    def test_next_item_segments_recommendation(self):

        # it 'rejects request with invalid recommId'
        req = RecommendNextItemSegments("invalid_recomm_id", 5)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
        # it 'rejects request to recommId which does not return item-segments'
        req = RecommendItemsToUser("entity_id", 3)
        resp = self.client.send(req)
        req = self.create_request(resp["recommId"], 5)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
