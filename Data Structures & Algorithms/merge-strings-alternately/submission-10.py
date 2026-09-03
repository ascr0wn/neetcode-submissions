class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        arr = []

        smallerlength, largerlength = (len(word1), len(word2)) if len(word1) < len(word2) else (len(word2), len(word1))

        for i in range(smallerlength):
            arr.append(word1[i])
            arr.append(word2[i])

        if smallerlength == len(word1):
            for i in range(smallerlength, largerlength):
                arr.append(word2[i])
            return "".join(arr)

        for i in range(smallerlength, largerlength):
            arr.append(word1[i])
        return "".join(arr)