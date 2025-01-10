#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

import time
from abc import ABC, abstractmethod
from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class RecommendItemSegmentsToItemTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,item_id,target_user_id,count,scenario=None,cascade_create=None,filter=None,booster=None,logic=None,expert_settings=None,return_ab_group=None):
        pass

    def test_recommend_item_segments_to_item(self):

        # it 'rejects request to scenario which is not set up'
        req = self.create_request('entity_id', 'entity_id', 5, scenario='scenario1', cascade_create=True)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)

