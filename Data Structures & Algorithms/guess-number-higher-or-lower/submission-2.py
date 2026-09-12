import random

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        guessed_num = random.randint(left, right)

        while guess(guessed_num) != 0:
            if guess(guessed_num) == 1:
                left = guessed_num + 1
                guessed_num = random.randint(left, right)
            else:
                right = guessed_num - 1
                guessed_num = random.randint(left, right)
        return guessed_num