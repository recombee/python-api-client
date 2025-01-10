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

class UpdateManualReqlSegmentTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,segmentation_id,segment_id,filter,title=None):
        pass

    def test_update_manual_reql_segment(self):

        # it 'updates manual ReQL segment'
        req = CreateManualReqlSegmentation('seg1', 'items', title='Test Segmentation', description='For test purposes')
        resp = self.client.send(req)
        req = AddManualReqlSegment('seg1', 'first-segment', '\'str_property\' != null', title='First Segment')
        resp = self.client.send(req)
        req = self.create_request('seg1', 'first-segment', '\'str_property\' == null', title='Updated Segment')
        resp = self.client.send(req)

