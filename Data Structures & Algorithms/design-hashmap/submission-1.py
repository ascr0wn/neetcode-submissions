class MyHashMap:

    def __init__(self):
        self.buckets = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        self.buckets[key] = value

    def get(self, key: int) -> int:
        return self.buckets[key]
        
    def remove(self, key: int) -> None:
        self.buckets[key] = -1