#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_search_synonyms import ListSearchSynonymsTest
from recombee_api_client.api_requests.list_search_synonyms import (
    ListSearchSynonyms,
    DEFAULT,
)


class ListSearchSynonymsTestCase(ListSearchSynonymsTest):

    def create_request(self, count=DEFAULT, offset=DEFAULT):
        return ListSearchSynonyms(count=count, offset=offset)
