#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class ListSearchSynonymsTest(RecombeeTest):

    def create_request(self,count=None,offset=None):
        pass

    def test_list_search_synonyms(self):

        # it 'lists search synonyms'
        req = AddSearchSynonym('sci-fi', 'science fiction')
        resp = self.client.send(req)
        req = self.create_request()
        resp = self.client.send(req)
        self.assertEqual(len(resp['synonyms']), 1)
        req = self.create_request(count=10, offset=1)
        resp = self.client.send(req)
        self.assertEqual(len(resp['synonyms']), 0)

