class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            length = len(nums)
            mid = length // 2

            if length == 1:
                return nums

            nums1 = mergeSort(nums[:mid])
            nums2 = mergeSort(nums[mid:])

            return merge(nums1, nums2)

        def merge(nums1, nums2):
            p1, p2, result, l1, l2 = 0, 0, [], len(nums1), len(nums2)
            while p1 < l1 and p2 < l2:
                if nums1[p1] <= nums2[p2]:
                    result.append(nums1[p1])
                    p1 += 1
                else:
                    result.append(nums2[p2])
                    p2 += 1
            while p1 < l1:
                result.append(nums1[p1])
                p1 += 1
            while p2 < l2:
                result.append(nums2[p2])
                p2 += 1
            return result

        return mergeSort(nums)
