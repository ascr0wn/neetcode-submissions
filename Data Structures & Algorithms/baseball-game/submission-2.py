#Extreme Optimisation!

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        push = stack.append # makeing stack.append local to rduce time
        for op in operations:
            if op == '+':
                push(stack[-1] + stack[-2]) # -1 gets last element
            elif op == 'D':
                push(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                push(int(op))
                
        return sum(stack)