class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0

        maxl, curr = 1, 1
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                curr += 1
            elif nums[i+1] == nums[i]:
                continue    
            else:
                maxl = max(maxl, curr)
                curr = 1
        maxl = max(maxl, curr)        
        return maxl            
        