#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class RecommendItemSegmentsToItemSegmentTest(RecombeeTest):

    def create_request(self,context_segment_id,target_user_id,count,scenario=None,cascade_create=None,filter=None,booster=None,logic=None,expert_settings=None,return_ab_group=None):
        pass

    def test_recommend_item_segments_to_item_segment(self):

        # it 'rejects request to scenario which is not set up'
        req = self.create_request('segment_id', 'entity_id', 5, scenario='scenario1', cascade_create=True)
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)

