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

class ListSegmentationsTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,source_type):
        pass

    def test_list_segmentations(self):

        time.sleep(10)
        # it 'lists existing segmentations'
        req = CreatePropertyBasedSegmentation('seg1', 'items', 'str_property')
        resp = self.client.send(req)
        req = self.create_request('items')
        resp = self.client.send(req)
        self.assertEqual(len(resp['segmentations']), 1)

