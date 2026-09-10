class MyQueue:

    def __init__(self):
        self.array = []
        self.front = 0

    def push(self, value: int) -> None:
        self.array.append(value)
        
    def pop(self) -> int:
        self.front += 1
        return self.array[self.front - 1]

    def peek(self) -> int:        
        return self.array[self.front]
    
    def empty(self) -> bool:
        return True if len(self.array) == self.front else False