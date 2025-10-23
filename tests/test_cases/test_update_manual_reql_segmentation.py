#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_manual_reql_segmentation import (
    UpdateManualReqlSegmentationTest,
)
from recombee_api_client.api_requests.update_manual_reql_segmentation import (
    UpdateManualReqlSegmentation,
    DEFAULT,
)


class UpdateManualReqlSegmentationTestCase(UpdateManualReqlSegmentationTest):

    def create_request(self, segmentation_id, title=DEFAULT, description=DEFAULT):
        return UpdateManualReqlSegmentation(
            segmentation_id, title=title, description=description
        )
