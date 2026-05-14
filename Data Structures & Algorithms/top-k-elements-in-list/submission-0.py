class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solutions = []
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for i, j in count.items():
            solutions.append([j, i])

        solutions.sort() 

        res = []
        while len(res) < k:
            res.append(solutions.pop()[1])
        return res           
        
            




        