#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

class RecombeeTest( unittest.TestCase ):

  def __init__(self, *args, **kwargs):
    super(RecombeeTest, self).__init__(*args, **kwargs)
    self.client = RecombeeClient('client-test', 'jGGQ6ZKa8rQ1zTAyxTc0EMn55YPF7FJLUtaMLhbsGxmvwxgTwXYqmUk5xVZFw98L')


  def setUp(self):

    self.client.send(ResetDatabase())

    batch = Batch([
      AddItem('entity_id'),
      AddUser('entity_id'),
      AddSeries('entity_id'),
      AddGroup('entity_id'),
      InsertToGroup('entity_id', 'item', 'entity_id'),
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
      AddBookmark('user', 'item', timestamp=0)
    ])

    self.client.send(batch)