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

class AddSearchSynonymTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,term,synonym,one_way=None):
        pass

    def test_add_search_synonym(self):

        # it 'adds search synonym'
        req = self.create_request('sci-fi', 'science fiction', one_way=True)
        resp = self.client.send(req)
        self.assertEqual(resp['term'], 'sci-fi')
        self.assertEqual(resp['synonym'], 'science fiction')
        req = self.create_request('sci-fi', 'science fiction', one_way=True)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)

