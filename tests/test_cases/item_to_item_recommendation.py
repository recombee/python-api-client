#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class ItemToItemRecommendationTest (RecommendationsTest ):

    def create_request(self,item_id,target_user_id,count,filter=None,booster=None,cascade_create=None,scenario=None,logic=None,return_properties=None,included_properties=None,user_impact=None,diversity=None,min_relevance=None,rotation_rate=None,rotation_time=None,expert_settings=None,return_ab_group=None):
        pass

    def test_item_to_item_recommendation(self):

        # it 'recommends'
        req = self.create_request('entity_id','entity_id',9)
        resp = self.client.send(req)
        # it 'recommends to previously nonexisting entity with cascadeCreate'
        req = self.create_request('nonexisting','entity_id',9,cascade_create=True)
        resp = self.client.send(req)
        # it 'recommends with expert settings'
        req = self.create_request('nonexisting2','entity_id',9,cascade_create=True,expert_settings={})
        resp = self.client.send(req)

