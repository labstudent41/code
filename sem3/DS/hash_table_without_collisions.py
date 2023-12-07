class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                # If the key already exissts, update its value
                item[1] = value
                return
        # If the key doesn't exist, add it to the list
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return

ht = HashTable(10)
ht.insert("apple", 5)
ht.insert("banana", 10)
ht.insert("cherry", 15)

print(ht.search("banana"))
ht.delete("banana")
print(ht.search("banana"))
