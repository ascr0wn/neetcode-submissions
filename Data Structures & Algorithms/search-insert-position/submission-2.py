import random
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            random_index = random.randint(left, right)
            if nums[random_index] == target:
                return random_index
            elif target > nums[random_index]:
                left = random_index + 1
            else:
                right = random_index - 1
        return left