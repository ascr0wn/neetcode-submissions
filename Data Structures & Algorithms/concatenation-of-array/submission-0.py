class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2 * length)
        index = 0
        for num in nums:
            ans[index] = num
            ans[index + length] = num
            index = index + 1
        return ans
