#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.test_cases.recombee_test import RecombeeTest
from recombee_api_client.api_requests import *

class BatchTestCase(RecombeeTest):

  def test_batch(self):
    reqs = [
          AddItemProperty('num', 'int'),
          AddItemProperty('time', 'timestamp'),
          SetItemValues('item1', {
                          'num': 99,
                          '!cascadeCreate': True}),
          AddItem('item1'),
          SetItemValues('item2', {
                          'num': 68,
                          'time': 27,
                          '!cascadeCreate': True}),
          ListItems(),
          ListItems(filter="'num' < 99"),
          DeleteItem('item1'),
          ListItems(filter="'num' >= 99"),
          AddCartAddition('user', 'item2',  timestamp='2013-10-29T09:38:41.341Z'),
          AddCartAddition('user', 'item2', cascade_create=True),
          RecommendItemsToItem('item2', 'user', 30),
          RecommendItemsToUser('user_id', 25, filter="'num'==68",cascade_create=True)
    ]

    resp = self.client.send(Batch(reqs))

    codes = [r['code'] for r in resp]
    self.assertEqual(codes, [201, 201, 200, 409, 200, 200, 200, 200, 200, 404, 200, 200, 200])
    self.assertEqual(sorted(resp[5]['json']), ['entity_id', 'item1', 'item2'])
    self.assertEqual(resp[6]['json'], ['item2'])
    self.assertEqual(resp[8]['json'], [])
    self.assertEqual(resp[12]['json']['recomms'], ['item2'])

  def test_large_batch(self):
    NUM = 23578
    reqs = [AddItem("item-%s" % i) for i in range(NUM)]
    resp = self.client.send(Batch(reqs))

    self.assertEqual(len(resp), NUM)

    for r in resp:
      self.assertEqual(r['code'], 201)
