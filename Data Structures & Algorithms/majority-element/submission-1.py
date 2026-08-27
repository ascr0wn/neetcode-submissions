class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict.get(num) + 1
                if count_dict.get(num) >= len(nums) / 2:
                    return num
            else:
                count_dict[num] = 1
                if count_dict.get(num) >= len(nums) / 2:
                    return num
            