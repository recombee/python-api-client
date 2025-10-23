#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_interaction import AddInteractionTest
from recombee_api_client.api_requests.add_bookmark import AddBookmark, DEFAULT


class AddBookmarkTestCase(AddInteractionTest):

    def create_request(
        self,
        user_id,
        item_id,
        timestamp=DEFAULT,
        cascade_create=DEFAULT,
        recomm_id=DEFAULT,
        additional_data=DEFAULT,
    ):
        return AddBookmark(
            user_id,
            item_id,
            timestamp=timestamp,
            cascade_create=cascade_create,
            recomm_id=recomm_id,
            additional_data=additional_data,
        )
