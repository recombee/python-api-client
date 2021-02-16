#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_search_synonyms import ListSearchSynonymsTest
from recombee_api_client.api_requests import *

class ListSearchSynonymsTestCase (ListSearchSynonymsTest):

    def create_request(self, count=None, offset=None):
        return ListSearchSynonyms(count=count, offset=offset)
