class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        size = len(nums)
        try:
            nums.index(val) 
        except ValueError:
            return size

        lastIndex = size - 1
        index = 0

        while (index < lastIndex):
            if nums[index] == val:
                if nums[lastIndex] == val:
                    lastIndex -= 1
                    continue
                else:
                    nums[index], nums[lastIndex] = nums[lastIndex], nums[index]
            index += 1
        return index