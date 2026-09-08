class Solution:
    def isValid(self, s: str) -> bool:
        array = []
        for char in s:
            if char in ['(','{','[']:
                array.append(char)
            else:
                if len(array) != 0 and char == ')' and array[len(array)-1] == '(':
                    array.pop(len(array) - 1)
                    continue
                elif len(array) != 0 and char == '}' and array[len(array)-1] == '{':
                    array.pop(len(array) - 1)
                    continue
                elif len(array) != 0 and (char == ']' and array[len(array)-1] == '['):
                    array.pop(len(array) - 1)
                    continue
                return False
        if len(array) > 0: return False
        else: return True
