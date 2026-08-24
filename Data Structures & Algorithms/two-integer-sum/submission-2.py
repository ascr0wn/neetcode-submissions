class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        ans = []

        for index in range(len(nums)):
            if nums[index] in dict.keys():
                if nums[index] * 2 == target:
                    ans.append(dict.get(nums[index]))
                    ans.append(index)
                    return ans
            dict[nums[index]] = index
        
        for index in range(len(nums)):
            num1 = nums[index]
            num2 = target - num1
            if dict.get(num2):
                if dict.get(num2) != index:
                    ans.append(index)
                    ans.append(dict.get(num2))
                    return ans
        return ans