class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while True:
            m=(l+r)>>1
            a = guess(m)
            if a==0:
                return m
            if a==1:
                l=m+1
            else:
                r=m-1