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
        self.queue = Stack()        

    def push(self, value: int) -> None:
        self.queue.push(value)

    def pop(self) -> int:
        if self.queue.size() > 1:
            temp = self.queue.pop()
            deleted_element = self.pop()
            self.queue.push(temp)
            return deleted_element
        return self.queue.pop()

    def peek(self) -> int:        
        if self.queue.size() > 1:
            temp = self.queue.pop()
            top_element = self.peek()
            self.queue.push(temp)
            return top_element
        return self.queue.top()
       
    def empty(self) -> bool:
       return self.queue.empty() 
