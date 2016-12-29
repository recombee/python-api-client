#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_item_interactions import ListItemInteractionsTest
from recombee_api_client.api_requests import *

class ListItemDetailViewsTestCase (ListItemInteractionsTest):

    def create_request(self, item_id):
        return ListItemDetailViews(item_id)
