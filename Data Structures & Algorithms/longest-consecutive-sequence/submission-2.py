class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0

        maxl = curr = 1
        arr = sorted(nums)
        
        for i in range(len(arr) - 1):
            if arr[i+1] == arr[i] + 1:
                curr += 1
            elif arr[i+1] == arr[i]:
                continue    
            else:
                maxl = max(maxl, curr)
                curr = 1
        maxl = max(maxl, curr)        
        return maxl            
        