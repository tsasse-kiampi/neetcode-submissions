class Solution:
    def reverseBits(self, n: int) -> int:
        c = bin(n)[2:]
        c = "0"*(32 - len(c)) + c
        c = c[::-1]
        return int(c, 2)
        