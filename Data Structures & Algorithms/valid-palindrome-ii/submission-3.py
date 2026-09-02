class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s) - 1

        while start < last:
            if s[start] == s[last]:
                start += 1
                last -= 1
            else:
                return self.check_palindrone(s[start+1:last+1]) or self.check_palindrone(s[start:last])
        return True

    def check_palindrone(self, s: str) -> bool:
        start = 0
        last = len(s) - 1
        
        while start < last:
            if s[start] != s[last]:
                return False
            start += 1
            last -= 1
        return True