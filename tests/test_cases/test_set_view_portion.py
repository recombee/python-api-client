#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.set_view_portion import SetViewPortionTest
from recombee_api_client.api_requests import *

class SetViewPortionTestCase (SetViewPortionTest):

    def create_request(self, user_id, item_id, portion, session_id=None, timestamp=None, cascade_create=None):
        return SetViewPortion(user_id, item_id, portion, session_id=session_id, timestamp=timestamp, cascade_create=cascade_create)
