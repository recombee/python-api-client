#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class SearchTest (RecommendationsTest ):

    def create_request(self,user_id,search_query,count,scenario=None,cascade_create=None,return_properties=None,included_properties=None,filter=None,booster=None,logic=None,expert_settings=None,return_ab_group=None):
        pass

    def test_search(self):

        # it 'finds "hello"'
        req = self.create_request('entity_id','hell',9)
        resp = self.client.send(req)
        self.assertEqual(len(resp['recomms']), 1)
        # it 'does not find random string'
        req = self.create_request('entity_id','sdhskldf',9)
        resp = self.client.send(req)
        self.assertEqual(len(resp['recomms']), 0)
        # it 'returnProperties'
        req = self.create_request('entity_id','hell',9,return_properties=True)
        resp = self.client.send(req)
        self.assertEqual(len(resp['recomms']), 1)

