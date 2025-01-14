#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from random import random

from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
from recombee_api_client.exceptions import *


class MissingEnvironmentVariable(Exception):
    pass


class RecombeeTest( unittest.TestCase ):

  def __init__(self, *args, **kwargs):
    super(RecombeeTest, self).__init__(*args, **kwargs)

    db_id = os.environ.get('DB_ID')
    if db_id is None:
      raise MissingEnvironmentVariable('DB_ID env var must be specified')

    token = os.environ.get('PRIVATE_TOKEN')
    if token is None:
      raise MissingEnvironmentVariable('PRIVATE_TOKEN env var must be specified')

    self.client = RecombeeClient(db_id, token, region=Region.EU_WEST)


  def setUp(self):

    self.client.send(ResetDatabase())

    while True:
      try:
        self.client.send(ListItems())
      except ResponseException as e:
        # Wait until DB is erased
        continue
      break

    batch = Batch([
      AddItem('entity_id'),
      AddUser('entity_id'),
      AddSeries('entity_id'),
      InsertToSeries('entity_id', 'item', 'entity_id', 1),
      AddItemProperty('int_property', 'int'),
      AddItemProperty('str_property', 'string'),
      SetItemValues('entity_id', {'int_property': 42, 'str_property': 'hello'}),
      AddUserProperty('int_property', 'int'),
      AddUserProperty('str_property', 'string'),
      SetUserValues('entity_id', {'int_property': 42, 'str_property': 'hello'})
    ])

    self.client.send(batch)


class InteractionsTest( RecombeeTest ):

  def setUp(self):

    super(InteractionsTest, self).setUp()

    batch = Batch([
      AddUser('user'),
      AddItem('item'),
      AddDetailView('user', 'item', timestamp=0),
      AddPurchase('user', 'item', timestamp=0),
      AddRating('user', 'item', 1, timestamp=0),
      AddCartAddition('user', 'item', timestamp=0),
      AddBookmark('user', 'item', timestamp=0),
      SetViewPortion('user', 'item', 1, timestamp=0),
    ])

    self.client.send(batch)

class RecommendationsTest( RecombeeTest ):

  def setUp(self):

    super(RecommendationsTest, self).setUp()

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
