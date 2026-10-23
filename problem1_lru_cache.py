class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self.capacity = capacity
        self.cache = {}

        # Dummy nodes simplify insertion and deletion.
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_most_recent(self, node):
        last = self.right.prev

        last.next = node
        node.prev = last

        node.next = self.right
        self.right.prev = node

    def get(self, key):
        
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert_most_recent(node)

        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert_most_recent(node)

        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.cache[lru_node.key]


def main():
    
    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)

    print("get(1):", cache.get(1))  # Expected: 10

    cache.put(3, 30)  # Evicts key 2 because key 1 was just used.

    print("get(2):", cache.get(2))  # Expected: -1
    print("get(3):", cache.get(3))  # Expected: 30

    cache.put(3, 300)
    print("get(3):", cache.get(3))  # Expected: 300

    empty_cache = LRUCache(0)
    empty_cache.put(1, 100)
    print("zero-capacity get(1):", empty_cache.get(1))  # Expected: -1


if __name__ == "__main__":
    main()