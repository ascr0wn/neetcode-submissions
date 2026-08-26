class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums.sort()

        try:
            i = nums.index(val) 
            index = nums.index(val) + 1
            count = 1
        except ValueError:
            return len(nums)

        while(index < len(nums)):
            if nums[index] == val:
                count += 1
                index += 1
                continue
            nums[i] = nums[index]
            i += 1
            index += 1
        
        return len(nums) - count
