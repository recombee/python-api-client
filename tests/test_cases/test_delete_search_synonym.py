#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_search_synonym import DeleteSearchSynonymTest
from recombee_api_client.api_requests import *

class DeleteSearchSynonymTestCase(DeleteSearchSynonymTest):

    def create_request(self, id):
        return DeleteSearchSynonym(id)
