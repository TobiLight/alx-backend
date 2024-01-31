#!/usr/bin/env python3
# File: 0-basic_cache.py
# Author: Oluwatobiloba Light
"""
Basic caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a simple caching system
    """

    def __init__(self):
        """
        Initializes a BasicCache instance with an empty cache_data dictionary.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary with the given key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        # if key and key in self.cache_data.keys():
        #     return self.cache_data[key]
        # return None
        return self.cache_data.get(key, None)  # shorter and cleaner ✔
