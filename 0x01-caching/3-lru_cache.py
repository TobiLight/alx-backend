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
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary with the given key.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lru_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        return self.cache_data.get(key, None)
