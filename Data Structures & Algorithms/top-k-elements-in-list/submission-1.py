import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count = 0
        current = nums[0]
        result = []
        flag = True
        max_heap = []
        for num in nums:
            if current == num:
                count += 1
            else:
                t1 = (0 - count, current)
                current = num
                count = 1
                heapq.heappush(max_heap, t1)
        heapq.heappush(max_heap, (0 - count, current))
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result

