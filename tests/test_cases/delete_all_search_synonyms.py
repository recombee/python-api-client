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

class DeleteAllSearchSynonymsTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self):
        pass

    def test_delete_all_search_synonyms(self):

        # it 'deletes all search synonyms'
        req = self.create_request()
        resp = self.client.send(req)

