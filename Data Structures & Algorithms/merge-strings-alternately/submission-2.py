class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = [""] * 200

        index1 = 0
        index2 = 1

        for character in word1:
            arr[index1] = character
            index1 += 2
        
        for character in word2:
            arr[index2] = character
            index2 += 2

        return "".join(arr)