#Dictionary Implementation!

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_dict = {}
        current_index = 0
        total = 0
        for op in operations:
            if op == '+':
                temp = my_dict[current_index - 1] + my_dict[current_index - 2]
                my_dict[current_index] = temp
                current_index += 1
                total += temp
            elif op == 'C':
                total -= my_dict.pop(current_index - 1)
                current_index -= 1
            elif op == 'D':
                temp = my_dict[current_index - 1] * 2
                my_dict[current_index] = temp
                current_index += 1
                total += temp
            else:
                my_dict[current_index] = int(op)
                current_index += 1
                total = total + int(op)
        return total
    