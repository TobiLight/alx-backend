#!/usr/bin/env python3
# File: 4-mru_cache.py
# Author: Oluwatobiloba Light
"""Most Recently Used Cache Module"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements Most Recently Used Caching system"""

    def __init__(self):
        """
        Initializes a BasicCache instance with an empty
        cache_data dictionary.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary with the given key.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
