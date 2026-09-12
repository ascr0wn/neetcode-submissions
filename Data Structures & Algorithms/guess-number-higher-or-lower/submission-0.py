# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        my_pick = int((left/2) + (right/2))

        while guess(my_pick) != 0:
            if guess(my_pick) == 1:
                left = my_pick + 1
                my_pick = int((left/2) + (right/2))
            else:
                right = my_pick - 1
                my_pick = int((left/2) + (right/2))
        return my_pick