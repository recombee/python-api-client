#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_interaction import AddInteractionTest
from recombee_api_client.api_requests.add_detail_view import AddDetailView, DEFAULT


class AddDetailViewTestCase(AddInteractionTest):

    def create_request(
        self,
        user_id,
        item_id,
        timestamp=DEFAULT,
        duration=DEFAULT,
        cascade_create=DEFAULT,
        recomm_id=DEFAULT,
        additional_data=DEFAULT,
        auto_presented=DEFAULT,
    ):
        return AddDetailView(
            user_id,
            item_id,
            timestamp=timestamp,
            duration=duration,
            cascade_create=cascade_create,
            recomm_id=recomm_id,
            additional_data=additional_data,
            auto_presented=auto_presented,
        )
