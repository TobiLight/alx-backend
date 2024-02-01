#!/usr/bin/env python3
# File: 2-lifo_cache.py
# Author: Oluwatobiloba Light
"""LIFO Cache module"""

from collections import OrderedDict, deque
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements a Last-in-First-Out caching system
    """

    def __init__(self):
        """
        Initializes a BasicCache instance with an empty
        cache_data dictionary.
        """
        self.stack = []
        # self.cache_data
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary with the given key.
        """
        if len(self.cache_data.items()) >= BaseCaching.MAX_ITEMS and key\
                not in self.cache_data.keys():
            popped_key = self.stack.pop()
            del self.cache_data[popped_key]
            print("DISCARD: {}".format(popped_key))

        if key is not None and item is not None:
            if key in self.cache_data.keys():
                key_idx_stack = self.stack.index(key)
                self.stack.pop(key_idx_stack)
                self.cache_data.pop(key)
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
            if key not in self.stack:
                self.stack.append(key)

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        return self.cache_data.get(key, None)
