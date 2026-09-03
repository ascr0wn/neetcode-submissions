class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        merged = "".join([a+b for a, b in zip(word1, word2)])
        
        return merged + ("".join(word1[len(word2): ]) + "".join(word2[len(word1): ]))