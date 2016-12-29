#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_entity import DeleteEntityTest
from recombee_api_client.api_requests import *

class DeleteSeriesTestCase (DeleteEntityTest):

    def create_request(self, series_id):
        return DeleteSeries(series_id)
