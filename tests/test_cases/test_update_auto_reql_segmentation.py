#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_auto_reql_segmentation import (
    UpdateAutoReqlSegmentationTest,
)
from recombee_api_client.api_requests.update_auto_reql_segmentation import (
    UpdateAutoReqlSegmentation,
    DEFAULT,
)


class UpdateAutoReqlSegmentationTestCase(UpdateAutoReqlSegmentationTest):

    def create_request(
        self, segmentation_id, expression=DEFAULT, title=DEFAULT, description=DEFAULT
    ):
        return UpdateAutoReqlSegmentation(
            segmentation_id, expression=expression, title=title, description=description
        )
