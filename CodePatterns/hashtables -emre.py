# https://emre.me/data-structures/hash-tables/

# Language	Name of Hash Table
# Java	HashMap, ConcurrentHashMap, HashTable
# Python	dict
# C++	std::unordered_map
# C#	Dictionary, Hashtable
# Ruby	Hash

# Implementation
# Lets summarize all of them with a complete Python Hash Table implementation.

class HashTable:
    def __init__(self):
        self.size = 13
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hashfunction(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hashfunction(self, key, size):
        return key % size  # remainder method

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size  # linear probing

    def get(self, key):
        start_slot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
        
# Now we can try our HashTable() implementation together.

hash_table = HashTable()
hash_table[99] = "cat"
hash_table[17] = "dog"
hash_table[54] = "lion"
hash_table[26] = "tiger"
hash_table[75] = "bird"
hash_table[31] = "cow"
hash_table[50] = "goat"
hash_table[69] = "pig"

print(hash_table.slots)
# Output: [26, None, 54, None, 17, 31, 69, None, 99, None, 75, 50, None]

print(hash_table.data)
# Output: ['tiger', None, 'lion', None, 'dog', 'cow', 'pig', None, 'cat', None, 'bird', 'goat', None]



