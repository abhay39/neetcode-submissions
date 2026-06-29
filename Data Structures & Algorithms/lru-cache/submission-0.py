class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1

        value = self.lru.pop(key)      # Remove
        self.lru[key] = value          # Reinsert at the end
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.pop(key)          # Remove old position

        self.lru[key] = value          # Insert at end

        if len(self.lru) > self.capacity:
            self.lru.pop(next(iter(self.lru)))   # Remove least recently used