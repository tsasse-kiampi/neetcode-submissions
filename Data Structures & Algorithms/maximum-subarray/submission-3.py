class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        res = [nums[0]]
        

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = 0
                for k in range(i, j+1):
                    s += nums[k]
                res.append(s)
        res.append(nums[-1])        

        return max(res)            

        