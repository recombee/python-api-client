#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_entity import DeleteEntityTest
from recombee_api_client.api_requests.delete_user import DeleteUser, DEFAULT


class DeleteUserTestCase(DeleteEntityTest):

    def create_request(self, user_id):
        return DeleteUser(user_id)
