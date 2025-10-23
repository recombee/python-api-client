#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_manual_reql_segment import UpdateManualReqlSegmentTest
from recombee_api_client.api_requests.update_manual_reql_segment import (
    UpdateManualReqlSegment,
    DEFAULT,
)


class UpdateManualReqlSegmentTestCase(UpdateManualReqlSegmentTest):

    def create_request(self, segmentation_id, segment_id, filter, title=DEFAULT):
        return UpdateManualReqlSegment(segmentation_id, segment_id, filter, title=title)
