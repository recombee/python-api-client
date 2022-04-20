#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_more_items import UpdateMoreItemsTest
from recombee_api_client.api_requests import *

class UpdateMoreItemsTestCase(UpdateMoreItemsTest):

    def create_request(self, filter, changes):
        return UpdateMoreItems(filter, changes)
