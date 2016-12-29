#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_interaction import AddInteractionTest
from recombee_api_client.api_requests import *

class AddBookmarkTestCase (AddInteractionTest):

    def create_request(self, user_id, item_id, timestamp=None, cascade_create=None):
        return AddBookmark(user_id, item_id, timestamp=timestamp, cascade_create=cascade_create)
