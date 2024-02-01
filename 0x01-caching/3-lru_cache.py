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
            self.cache_data[key] = item
            if key not in self.lru:
                self.lru.append(key)
            else:
                self.lru.append(
                    self.lru.pop(self.lru.index(key)))
            if len(self.lru) > BaseCaching.MAX_ITEMS:
                discard = self.lru.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        return self.cache_data.get(key, None)
