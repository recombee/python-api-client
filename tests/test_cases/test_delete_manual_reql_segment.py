#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_manual_reql_segment import DeleteManualReqlSegmentTest
from recombee_api_client.api_requests import *

class DeleteManualReqlSegmentTestCase(DeleteManualReqlSegmentTest):

    def create_request(self, segmentation_id, segment_id):
        return DeleteManualReqlSegment(segmentation_id, segment_id)
