class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        second = 1
        space = False

        while second < len(nums):
            if nums[first] == nums[second]:
                second += 1
                space = True
                continue
            if space:
                first += 1
                nums[first] = nums[second]
                second += 1
                continue
            first += 1
            second += 1
        return first+1