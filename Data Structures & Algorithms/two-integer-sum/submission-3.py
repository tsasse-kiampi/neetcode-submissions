class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_record = {}

        for i in range(len(nums)):
            if target - nums[i] in h_record:
                return [h_record[target - nums[i]], i]
            else: 
                h_record[nums[i]] = i   
                        
        