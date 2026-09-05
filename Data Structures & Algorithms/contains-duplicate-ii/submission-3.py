class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for index, num in enumerate(nums):
            if num in my_dict:
                return True
            
            my_dict[num] = index

            if len(my_dict) > k:
                del my_dict[nums[index-k]]

        return False