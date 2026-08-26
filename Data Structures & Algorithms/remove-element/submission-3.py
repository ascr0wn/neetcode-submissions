class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        insertIndex = 0

        for index in range(len(nums)):
            if nums[index] != val:
                nums[insertIndex] = nums[index]
                insertIndex += 1
        return insertIndex