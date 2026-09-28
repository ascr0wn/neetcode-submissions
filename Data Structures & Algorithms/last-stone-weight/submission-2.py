class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index, num in enumerate(stones):
            stones[index] = -num
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                break
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            result = stone1 - stone2
            if result == 0:
                continue
            heapq.heappush(stones, result)
        if stones:
            return abs(heapq.heappop(stones))
        return 0