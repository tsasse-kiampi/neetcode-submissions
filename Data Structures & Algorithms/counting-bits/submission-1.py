class Solution:
    def countBits(self, n: int) -> List[int]:

        nums = [0]
        
        
        for i in range(1, n + 1):
            c = nums[(i >> 1)] + (i & 1)
            nums.append(c)
        return nums     

           

