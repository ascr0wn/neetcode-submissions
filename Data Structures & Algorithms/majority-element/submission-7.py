class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)

        if length % 2 == 0:
            if nums[length // 2 - 1] == nums[0]:
                return nums[0]
            else:
                return nums[length - 1]
        
        if nums[0] == nums[length // 2]:
            return nums[0]
        elif nums[length // 2 - 1] == nums[length // 2]:
            return nums[length //2 - 1]
        return nums[length // 2 + 1]