class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_bits = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            tmp = ((a&b)<<1)&max_bits
            a = (a^b)&max_bits
            b = tmp
        return a if a < max_int else ~(a^max_bits)   

        