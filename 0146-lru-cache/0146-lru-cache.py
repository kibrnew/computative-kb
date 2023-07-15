class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.track = {}

    def get(self, key: int) -> int:
        if key in self.track:
            self.stack.remove(key)
            self.stack.append(key)
            return self.track[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.track:
            self.track[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        elif len(self.stack) < self.capacity:
            self.stack.append(key)
            self.track[key] = value
        else:
            cache = self.stack.pop(0)
            del self.track[cache]
            self.stack.append(key)
            self.track[key] = value

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)