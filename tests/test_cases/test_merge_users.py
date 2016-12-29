#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.merge_users import MergeUsersTest
from recombee_api_client.api_requests import *

class MergeUsersTestCase (MergeUsersTest):

    def create_request(self, target_user_id, source_user_id, keep_source_user=None, cascade_create=None):
        return MergeUsers(target_user_id, source_user_id, keep_source_user=keep_source_user, cascade_create=cascade_create)
