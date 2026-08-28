class MyHashSet:
    def __init__(self):
        self.MyHashMap = [False] * 1000001

    def add(self, key: int):
        self.MyHashMap[key] = True

    def remove(self, key: int):
        self.MyHashMap[key] = False

    def contains(self, key: int) -> bool:
        return self.MyHashMap[key]
