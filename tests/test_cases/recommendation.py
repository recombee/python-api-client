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

class RecommendationTest(RecommendationsTest, ABC):

    @abstractmethod
    def create_request(self,user_id,count,scenario=None,cascade_create=None,return_properties=None,included_properties=None,filter=None,booster=None,logic=None,diversity=None,expert_settings=None,return_ab_group=None):
        pass

    def test_recommendation(self):

        # it 'recommends'
        req = self.create_request('entity_id', 9)
        resp = self.client.send(req)
        # it 'recommends to previously nonexisting entity with cascadeCreate'
        req = self.create_request('nonexisting', 9, cascade_create=True)
        resp = self.client.send(req)
        # it 'recommends with expert settings'
        req = self.create_request('nonexisting2', 9, cascade_create=True, expert_settings={})
        resp = self.client.send(req)

