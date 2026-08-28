class MyHashSet:
    def __init__(self):
        self.hashset_array = [[] for _ in range(1000)]

    def add(self, key: int):
        location = self.calculate_hash(key)
        if key in self.hashset_array[location]:
                return
        self.hashset_array[location].append(key)
        return

    def calculate_hash(self, key: int) -> int:
        return key % 1000

    def remove(self, key: int):
        location = self.calculate_hash(key)
        try:
            self.hashset_array[location].remove(key)
            return
        except ValueError:
            return

    def contains(self, key: int) -> bool:
        location = self.calculate_hash(key)
        return key in self.hashset_array[location]