class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        left = [1]*len(nums)
        right = [1]*len(nums)

        prodl = 1
        for i in range(1, len(nums)):
            prodl *= nums[i-1]
            left[i] = prodl

        prodr = 1
        for i in range(len(nums)-2, -1, -1):
            prodr *= nums[i+1]
            right[i] = prodr

        for i in range(len(nums)):
            res[i] = left[i]*right[i]

        return res    
        