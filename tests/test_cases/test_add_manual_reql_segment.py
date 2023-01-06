#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_manual_reql_segment import AddManualReqlSegmentTest
from recombee_api_client.api_requests import *

class AddManualReqlSegmentTestCase(AddManualReqlSegmentTest):

    def create_request(self, segmentation_id, segment_id, filter, title=None):
        return AddManualReqlSegment(segmentation_id, segment_id, filter, title=title)
