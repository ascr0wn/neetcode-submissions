class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m-1
        index2 = n-1
        index1last = m + n - 1
        while index2 >= 0:
            if index1 < 0:
                nums1[index1last] = nums2[index2]
                index1last -= 1
                index2 -= 1
            else:
                if nums1[index1] > nums2[index2]:
                    nums1[index1last] = nums1[index1]
                    index1 -= 1
                    index1last -= 1
                elif nums1[index1] <= nums2[index2]:
                    nums1[index1last] = nums2[index2]
                    index2 -= 1
                    index1last -= 1