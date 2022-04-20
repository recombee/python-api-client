#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_more_items import DeleteMoreItemsTest
from recombee_api_client.api_requests import *

class DeleteMoreItemsTestCase(DeleteMoreItemsTest):

    def create_request(self, filter):
        return DeleteMoreItems(filter)
