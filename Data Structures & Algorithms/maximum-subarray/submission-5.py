class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        #res = [nums[0]]
        res = []

        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                res.append(s)
        res.append(nums[-1])        

        return max(res)            

        