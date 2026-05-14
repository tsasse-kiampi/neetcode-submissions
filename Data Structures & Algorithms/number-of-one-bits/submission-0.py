class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0

        while n >= 1:
            s += (n & 1)
            n//=2

        return s    
        