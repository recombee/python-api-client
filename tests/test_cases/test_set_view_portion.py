#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.set_view_portion import SetViewPortionTest
from recombee_api_client.api_requests.set_view_portion import SetViewPortion, DEFAULT


class SetViewPortionTestCase(SetViewPortionTest):

    def create_request(
        self,
        user_id,
        item_id,
        portion,
        session_id=DEFAULT,
        timestamp=DEFAULT,
        cascade_create=DEFAULT,
        recomm_id=DEFAULT,
        additional_data=DEFAULT,
        auto_presented=DEFAULT,
        time_spent=DEFAULT,
    ):
        return SetViewPortion(
            user_id,
            item_id,
            portion,
            session_id=session_id,
            timestamp=timestamp,
            cascade_create=cascade_create,
            recomm_id=recomm_id,
            additional_data=additional_data,
            auto_presented=auto_presented,
            time_spent=time_spent,
        )
