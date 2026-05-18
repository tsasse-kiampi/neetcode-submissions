class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        else:
            return min (
                self.findMin(nums[:n//2]),
                self.findMin(nums[n//2:])
            )
        