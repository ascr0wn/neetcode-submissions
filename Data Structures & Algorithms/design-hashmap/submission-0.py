class MyHashMap:

    def __init__(self):
        self.buckets = [[]for _ in range(1009)]
        

    def put(self, key: int, value: int) -> None:
        self.location = self.calculate_hash(key)
        for index in self.buckets[self.location]:
            if index[0] == key:
                index[1] = value
                return
        self.buckets[self.location].extend([[key, value]])


    def get(self, key: int) -> int:
        self.location = self.calculate_hash(key)
        for index in self.buckets[self.location]:
            if index[0] == key:                   
                return index[1]
        return -1
        
        

    def remove(self, key: int) -> None:
        self.location = self.calculate_hash(key)
        for index in self.buckets[self.location]:
            if index[0] == key:
                index[1] = -1
                return
        return


    def calculate_hash(self, key: int) -> int:
        return key % 1009
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)