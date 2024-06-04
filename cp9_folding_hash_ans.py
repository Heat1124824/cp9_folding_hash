class FoldingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def folding_hash(self, key):
        key_str = str(key)
        part_size = 3
        total_sum = 0

        for i in range(0, len(key_str), part_size):
            part = key_str[i:i + part_size]
            total_sum += int(part)

        return total_sum % self.size

    def insert(self, key, value):
        index = self.folding_hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self.folding_hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def display(self):
        for i, items in enumerate(self.table):
            print(f"Index {i}: {items}")

hash_table = FoldingHashTable(10)
# hash_table.insert(510315, "Belladonna")
# hash_table.insert(622188, "Faye")
# hash_table.insert(708298, "Philomena")
hash_table.insert(353181, "Penina")
hash_table.insert(110618, "Zetta")
hash_table.insert(922745, "Tequila")

hash_table.display()

# print("Search for key 510315:", hash_table.search(510315))
# print("Search for key 708298:", hash_table.search(708298))
# print("Search for key 510612:", hash_table.search(510612))
print("Search for key 353181:", hash_table.search(353181))
print("Search for key 922745:", hash_table.search(922745))
print("Search for key 110011:", hash_table.search(110011))
