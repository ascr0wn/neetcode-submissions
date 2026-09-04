class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myhashset = set(nums)
        temp = list(myhashset)
        temp.sort()
        print(temp)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)