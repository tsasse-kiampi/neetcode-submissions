class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_record = {}

        for i in range(len(nums)):
            if target - nums[i] not in h_record:
                h_record[nums[i]] = i
            else:    
                return [h_record[target - nums[i]], i]        
        