

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:

            """replacing data for same key"""
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:

                """hash until slot is None or slot key is the same"""
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                """if slot is None then add key and data"""
                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    """if key is the same replace data"""
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and found is False and stop is False:

            """found key"""
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))

                """Check all slot"""
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

    def hash(self, word):
        h = 0
        for ch in word:
            h *= 37
            h += ord(ch)
        return h




H = HashTable()
# H.put(54, "cat")
# H.put(26, "dog")
# H.put(93, "lion")
# H.put(17, "tiger")
# H.put(77, "bird")
# H.put(31, "cow")
# H.put(44, "goat")
# H.put(55, "pig")
# H.put(20, "chicken")


print(H.slots)
print(H.data)

"""set new item for the existing key"""
# H.__setitem__(20, "duck")

# print(H.slots)
# print(H.data)





