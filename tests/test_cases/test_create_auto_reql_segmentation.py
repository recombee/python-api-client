#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.create_auto_reql_segmentation import (
    CreateAutoReqlSegmentationTest,
)
from recombee_api_client.api_requests.create_auto_reql_segmentation import (
    CreateAutoReqlSegmentation,
    DEFAULT,
)


class CreateAutoReqlSegmentationTestCase(CreateAutoReqlSegmentationTest):

    def create_request(
        self,
        segmentation_id,
        source_type,
        expression,
        title=DEFAULT,
        description=DEFAULT,
    ):
        return CreateAutoReqlSegmentation(
            segmentation_id,
            source_type,
            expression,
            title=title,
            description=description,
        )
