#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

import time
from abc import ABC, abstractmethod
from tests.test_cases.recombee_test import (
    RecombeeTest,
    InteractionsTest,
    RecommendationsTest,
)
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *


class AddItemPropertyTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self, property_name, type, role=None, metadata=None):
        pass

    def test_add_item_property(self):

        # it 'does not fail with valid name and type'
        req = self.create_request("number", "int")
        resp = self.client.send(req)
        req = self.create_request("str", "string")
        resp = self.client.send(req)
        # it 'fails with invalid type'
        req = self.create_request("prop", "integer")
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
        # it 'really stores property to the system'
        req = self.create_request("number2", "int")
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)
        # it 'does not fail with valid property role and metadata'
        req = self.create_request("title", "string", role="title")
        resp = self.client.send(req)
        # it 'fails with duplicate property role or invalid metadata'
        req = self.create_request("str4", "string", role="summary")
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)
        req = self.create_request("str5", "string", role="titl")
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)
