#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_view_portion import DeleteViewPortionTest
from recombee_api_client.api_requests import *

class DeleteViewPortionTestCase (DeleteViewPortionTest):

    def create_request(self, user_id, item_id, session_id=None):
        return DeleteViewPortion(user_id, item_id, session_id=session_id)
