class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        else:
            return min (
                self.findMin(nums[:len(nums)//2]),
                self.findMin(nums[len(nums)//2:])
            )
        