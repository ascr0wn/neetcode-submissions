class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                low = mid + 1
            else:
                high = mid - 1
        return low if low**2 == x else low - 1