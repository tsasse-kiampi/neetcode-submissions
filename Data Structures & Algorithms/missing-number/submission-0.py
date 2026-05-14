class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        s = sum(nums)
        return len(nums)*(1 + len(nums))//2 - s
        