#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.remove_from_group import RemoveFromGroupTest
from recombee_api_client.api_requests import *

class RemoveFromGroupTestCase (RemoveFromGroupTest):

    def create_request(self, group_id, item_type, item_id):
        return RemoveFromGroup(group_id, item_type, item_id)
