from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move the key to the end to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Remove old value so we can update the position
            self.cache.move_to_end(key)
        self.cache[key] = value
        # Remove least recently used if capacity exceeded
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove first inserted (LRU)

# Test
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))    # Output: 1
lru.put(3, 3)        # Evicts key 2
print(lru.get(2))    # Output: -1 (not found)
lru.put(4, 4)        # Evicts key 1
print(lru.get(1))    # Output: -1 (not found)
print(lru.get(3))    # Output: 3
print(lru.get(4))    # Output: 4
