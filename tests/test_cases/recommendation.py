#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import random

from tests.test_cases.recombee_test import RecombeeTest
from recombee_api_client.api_requests import *

class RecommendationTest(RecombeeTest):

  def create_request(entity_id, count, optional = dict()):
    pass

  def setUp(self):

    super(RecommendationTest, self).setUp()

    num = 1000
    probability_purchased = 0.007


    my_users = ["user-%s" % i for i in range(num)]
    my_items = ["item-%s" % i for i in range(num)]

    my_purchases = []
    for user in my_users:
      p = [it for it in my_items if random() < probability_purchased]
      for item in p:
        my_purchases.append({'userId': user, 'itemId': item} )

    self.client.send(Batch([AddUser(u) for u in my_users]))
    self.client.send(Batch([AddItemProperty('answer', 'int'), AddItemProperty('id2', 'string'), AddItemProperty('empty', 'string')]))
    self.client.send(Batch([SetItemValues(item_id, {'answer': 42, 'id2': item_id, '!cascadeCreate': True}) for item_id in my_items]))
    self.client.send(Batch([AddPurchase(p['userId'], p['itemId']) for p in my_purchases ]))

  def test_basic_recomm(self):
    req = self.create_request('entity_id', 9)
    res = self.client.send(req)
    self.assertEqual(len(res), 9)

  def test_rotation(self):
    req = self.create_request('entity_id', 9)
    recommended1 = self.client.send(req)
    self.assertEqual(len(recommended1), 9)

    req = self.create_request('entity_id', 9, rotation_rate=1)
    recommended2 = self.client.send(req)
    self.assertEqual(len(recommended2), 9)

    for item_id in recommended1:
      self.assertNotIn(item_id, recommended2)


  def test_in_batch(self):
    num = 7;
    reqs = [self.create_request('entity_id', 9) for _ in range(num) ]
    self.client.send(Batch(reqs))
    
  def test_returning_properties(self):
    req = self.create_request('entity_id', 9, return_properties=True, included_properties=['answer', 'id2', 'empty'])
    recommended = self.client.send(req)

    for rec in recommended:
      self.assertEqual(rec['id2'], rec['itemId'])
      self.assertEqual(rec['answer'], 42)
      self.assertIn('empty', rec)

    req = self.create_request('entity_id', 9, return_properties=True, included_properties='answer,id2')
    recommended = self.client.send(req)

    for rec in recommended:
      self.assertEqual(rec['id2'], rec['itemId'])
      self.assertEqual(rec['answer'], 42)
      self.assertNotIn('empty', rec)