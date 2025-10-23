#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_entity import DeleteEntityTest
from recombee_api_client.api_requests.delete_series import DeleteSeries, DEFAULT


class DeleteSeriesTestCase(DeleteEntityTest):

    def create_request(self, series_id, cascade_delete=DEFAULT):
        return DeleteSeries(series_id, cascade_delete=cascade_delete)
