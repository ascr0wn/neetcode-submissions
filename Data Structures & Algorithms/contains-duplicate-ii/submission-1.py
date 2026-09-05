class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = i
                continue
            if abs(my_dict[nums[i]] - i) <= k:
                return True
            my_dict[nums[i]] = i
        return False