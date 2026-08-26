class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        insertIndex = 0

        for num in nums:
            if num != val:
                nums[insertIndex] = num
                insertIndex += 1
        return insertIndex