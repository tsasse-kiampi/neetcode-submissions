class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h_record = {}

        for i in range(n):
            if target - nums[i] in h_record:
                return [h_record[target - nums[i]], i]
            
            h_record[nums[i]] = i   
                        
        