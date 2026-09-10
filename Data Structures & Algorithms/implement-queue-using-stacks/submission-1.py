class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value:int):
        self.stack.append(value)
    
    def pop(self) -> int:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[self.size() - 1]

    def empty(self) -> bool:
        if self.size() == 0:
            return True
        else: 
            return False

    def size(self) -> int:
        return len(self.stack)

class MyQueue:

    def __init__(self):
        self.queue1 = Stack()    
        self.queue2 = Stack()    

    def push(self, value: int) -> None:
        for _ in range(self.queue1.size()):
            self.queue2.push(self.queue1.pop())
        self.queue2.push(value)
        for _ in range(self.queue2.size()):
            self.queue1.push(self.queue2.pop())

    def pop(self) -> int:
        return self.queue1.pop()

    def peek(self) -> int:        
        return self.queue1.top()
    
    def empty(self) -> bool:
       return self.queue1.empty() 
