#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_search_synonym import AddSearchSynonymTest
from recombee_api_client.api_requests import *

class AddSearchSynonymTestCase(AddSearchSynonymTest):

    def create_request(self, term, synonym, one_way=None):
        return AddSearchSynonym(term, synonym, one_way=one_way)
