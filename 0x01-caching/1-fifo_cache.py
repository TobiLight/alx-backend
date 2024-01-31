#!/usr/bin/env python3
# File: 1-fifo_cache.py
# Author: Oluwatobiloba Light
"""
FIFOCache module
"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a First-in-First-Out caching system
    """

    def __init__(self):
        """
        Initializes a BasicCache instance with an empty
        cache_data dictionary.
        """
        self.cached_keys = deque()
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary with the given key.
        """
        if key is not None and item is not None:
            self.cached_keys.append(key)
            self.cache_data[key] = item

        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            popped_key = self.cached_keys.popleft()
            del self.cache_data[popped_key]
            print("DISCARD: {}".format(popped_key))

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        return self.cache_data.get(key, None)  # shorter and cleaner ✔
