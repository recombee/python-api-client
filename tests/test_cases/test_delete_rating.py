#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_interaction import DeleteInteractionTest
from recombee_api_client.api_requests.delete_rating import DeleteRating, DEFAULT


class DeleteRatingTestCase(DeleteInteractionTest):

    def create_request(self, user_id, item_id, timestamp=DEFAULT):
        return DeleteRating(user_id, item_id, timestamp=timestamp)
