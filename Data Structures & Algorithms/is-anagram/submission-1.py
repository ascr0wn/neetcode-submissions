class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        for index1 in range(len(s)):
            if s[index1] in dict1:
                dict1[s[index1]] = dict1[s[index1]] + 1
            else:
                dict1[s[index1]] = 1

        for index1 in range(len(t)):
            if t[index1] in dict1:
                dict1[t[index1]] = dict1[t[index1]] - 1
                if dict1[t[index1]] == 0:
                    del dict1[t[index1]]
            else:
                return False
        return True