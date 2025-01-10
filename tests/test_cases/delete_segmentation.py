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

class DeleteSegmentationTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,segmentation_id):
        pass

    def test_delete_segmentation(self):

        # it 'deletes segmentation'
        req = CreatePropertyBasedSegmentation('seg1', 'items', 'str_property')
        resp = self.client.send(req)
        req = self.create_request('seg1')
        resp = self.client.send(req)
        req = self.create_request('seg1')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

