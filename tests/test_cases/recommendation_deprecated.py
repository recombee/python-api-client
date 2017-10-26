#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class RecommendationDeprecatedTest (RecommendationsTest ):

    def create_request(self,user_id,count,filter=None,booster=None,allow_nonexistent=None,cascade_create=None,scenario=None,return_properties=None,included_properties=None,diversity=None,min_relevance=None,rotation_rate=None,rotation_time=None,expert_settings=None):
        pass

    def test_recommendation_deprecated(self):

        # it 'recommends'
        req = self.create_request('entity_id',9)
        resp = self.client.send(req)
        self.assertEqual(len(resp), 9)
        # it 'recommends to previously nonexisting entity with cascadeCreate'
        req = self.create_request('nonexisting',9,cascade_create=True)
        resp = self.client.send(req)
        self.assertEqual(len(resp), 9)
        # it 'recommends with expert settings'
        req = self.create_request('nonexisting2',9,cascade_create=True,expert_settings={})
        resp = self.client.send(req)
        self.assertEqual(len(resp), 9)

