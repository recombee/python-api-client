#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.insert_to_series import InsertToSeriesTest
from recombee_api_client.api_requests.insert_to_series import InsertToSeries, DEFAULT


class InsertToSeriesTestCase(InsertToSeriesTest):

    def create_request(
        self, series_id, item_type, item_id, time, cascade_create=DEFAULT
    ):
        return InsertToSeries(
            series_id, item_type, item_id, time, cascade_create=cascade_create
        )
