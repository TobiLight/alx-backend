#!/usr/bin/env python3
# File: 3-lru_cache.py
# Author: Oluwatobiloba Light
"""LRU Cache Module"""

from collections import deque
from typing import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Implements a Least Recently Used Caching system
    """

    def __init__(self):
        """
        Initializes a BasicCache instance with an empty
        cache_data dictionary.
        """
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary with the given key.
        """
        if key is not None and item is not None:
            if len(self.lru) > BaseCaching.MAX_ITEMS:
                popped_key = self.lru.pop(0)
                del self.cache_data[popped_key]
                print('popped_key: {}'.format(popped_key))
            self.cache_data[key] = item
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        if key is not None and key in self.cache_data:
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            return self.cache_data[key]
        return self.cache_data.get(key, None)
