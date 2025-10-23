#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_interaction import DeleteInteractionTest
from recombee_api_client.api_requests.delete_detail_view import (
    DeleteDetailView,
    DEFAULT,
)


class DeleteDetailViewTestCase(DeleteInteractionTest):

    def create_request(self, user_id, item_id, timestamp=DEFAULT):
        return DeleteDetailView(user_id, item_id, timestamp=timestamp)
