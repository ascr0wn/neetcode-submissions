class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        matrix = list(dict.items())
        matrix.sort(key=lambda x: x[1])
        index = -1
        result = []
        for _ in range(k):
            result.append(matrix[index][0])
            index -= 1
        return result