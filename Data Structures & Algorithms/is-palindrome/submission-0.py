class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        print(s1)
        start = 0
        last = len(s1) - 1
        while start < last:
            if not s1[start].isalnum():
                start += 1
                continue
            if not s1[last].isalnum():
                last -= 1
                continue
            if s1[start] != s1[last]:
                return False
            start, last = start+1, last-1
        return True