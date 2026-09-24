from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move the accessed item to the end (marks it as most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If key exists, moving it to the end updates its recency status
        if key in self.cache:
            self.cache.move_to_end(key)
            
        # Insert or update the value
        self.cache[key] = value
        
        # If we exceeded the capacity, remove the least recently used item (the first one)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)