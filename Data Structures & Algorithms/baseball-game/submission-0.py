class Solution:

    def __init__(self):
        self.my_stack = []
        self.total = 0

    def calPoints(self, operations: List[str]) -> int:
        for op in operations:
            if op == '+':
                self.add_scores()
            elif op == 'C':
                self.reduce_score()
            elif op == 'D':
                self.double_score()
            else:
                self.add_score(int(op))
        return self.total

    def add_score(self, value: int):
        self.my_stack.append(value)
        self.total = self.total + value

    def add_scores(self):
        self.my_stack.append(self.my_stack[len(self.my_stack) - 1] + self.my_stack[len(self.my_stack) - 2])
        self.total = self.total + self.my_stack[len(self.my_stack) - 1]

    def reduce_score(self):
        self.total = self.total - self.my_stack.pop()

    def double_score(self):
        self.my_stack.append(self.my_stack[len(self.my_stack) - 1] * 2)
        self.total = self.total + self.my_stack[len(self.my_stack) - 1]
