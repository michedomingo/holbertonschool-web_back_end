#!/usr/bin/python3
"""
Defines BasicCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ Add key/value pair to cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns value in self.cache_data linked to key """
        return self.cache_data.get(key)
