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


class CompositeRecommendationTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(
        self,
        scenario,
        count,
        item_id=None,
        user_id=None,
        logic=None,
        segment_id=None,
        cascade_create=None,
        source_settings=None,
        result_settings=None,
        expert_settings=None,
    ):
        pass

    def test_composite_recommendation(self):

        # it 'rejects request to scenario which is not set up'
        req = self.create_request("scenario_id", 5, cascade_create=True)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
