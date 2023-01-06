#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_manual_reql_segment import UpdateManualReqlSegmentTest
from recombee_api_client.api_requests import *

class UpdateManualReqlSegmentTestCase(UpdateManualReqlSegmentTest):

    def create_request(self, segmentation_id, segment_id, filter, title=None):
        return UpdateManualReqlSegment(segmentation_id, segment_id, filter, title=title)
