#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_item_interactions import ListItemInteractionsTest
from recombee_api_client.api_requests.list_item_purchases import (
    ListItemPurchases,
    DEFAULT,
)


class ListItemPurchasesTestCase(ListItemInteractionsTest):

    def create_request(self, item_id):
        return ListItemPurchases(item_id)
