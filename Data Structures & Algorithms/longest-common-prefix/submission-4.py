class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        hashset = set()

        index = 0

        for i in range(len(strs[0])):
            hashset.add(strs[0][0:i+1])
            for str in strs:
                if str[0:i+1] not in hashset:
                    return strs[0][0:i]
            index = i
            hashset.remove(strs[0][0:i+1])
        return strs[0][0:index+1]

