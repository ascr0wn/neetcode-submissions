class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                print(f"curent left: {left}, right: {right} -> left: {left}, right: {mid-1}")
                right = mid - 1
            else:
                print(f"curent left: {left}, right: {right} -> left: {mid + 1}, right: {right}")
                left = mid + 1
        return -1