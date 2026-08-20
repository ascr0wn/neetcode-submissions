class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2 * length)
        index = 0
        for index in range(length):
            ans[index] = nums[index]
            ans[index + length] = nums[index]
            index = index + 1
        return ans
