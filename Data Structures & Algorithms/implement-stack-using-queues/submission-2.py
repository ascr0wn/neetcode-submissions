from collections import deque

class Queue:
    def __init__(self):
        self._q = deque()
        
    def push(self, val: int) -> None:
        """Pushes an element to the back of the queue."""
        self._q.append(val)
        
    def pop(self) -> int:
        """Removes and returns the element from the front of the queue."""
        if self.empty():
            raise IndexError("pop from empty queue")
        return self._q.popleft()
        
    def peek(self) -> int:
        """Returns the element at the front of the queue without removing it."""
        if self.empty():
            raise IndexError("peek from empty queue")
        return self._q[0]
        
    def size(self) -> int:
        """Returns the number of elements in the queue."""
        return len(self._q)
        
    def empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return len(self._q) == 0

class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.push(x)
        for _ in range(self.q.size() - 1):
            self.q.push(self.q.pop())

    def pop(self)-> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q.peek()

    def empty(self) -> bool:
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()