class Solution:
    def countBits(self, n: int) -> List[int]:

        nums = []
        
        
        for i in range(n + 1):
            b = bin(i)[2:]
            s = 0
            for j in range(len(b)):
                s += int(b[j])

            nums.append(s)   

        return nums     

           

