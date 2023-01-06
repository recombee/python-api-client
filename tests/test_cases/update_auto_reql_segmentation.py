#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class UpdateAutoReqlSegmentationTest(RecombeeTest):

    def create_request(self,segmentation_id,expression=None,title=None,description=None):
        pass

    def test_update_auto_reql_segmentation(self):

        # it 'updates auto ReQL segmentation'
        req = CreateAutoReqlSegmentation('seg1', 'items', '{\'str_property\'}', title='Test Segmentation', description='For test purposes')
        resp = self.client.send(req)
        req = self.create_request('seg1', title='New title', expression='{\'str_property\' + \'str_property\'}', description='Updated')
        resp = self.client.send(req)

