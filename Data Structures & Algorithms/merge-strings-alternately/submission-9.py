class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        length1 = len(word1)
        length2 = len(word2)
        count1 = 0
        count2 = 0

        while count1 < length1 and count2 < length2:
            word.append(word1[count1])
            word.append(word2[count2])
            count1 += 1
            count2 += 1

        while count1 < length1:
            word.append(word1[count1])
            count1 += 1

        while count2 < length2:
            word.append(word2[count2])
            count2 += 1
        
        return "".join(word)
