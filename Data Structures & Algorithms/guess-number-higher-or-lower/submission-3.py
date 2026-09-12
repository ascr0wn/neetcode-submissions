import random

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        guessed_num = (left + right) >> 1
        answer = guess(guessed_num)

        while answer != 0:
            if answer == 1:
                left = guessed_num + 1
                guessed_num = left + right >> 1
                answer = guess(guessed_num)
            else:
                right = guessed_num - 1
                guessed_num = left + right >> 1
                answer = guess(guessed_num)
        return guessed_num