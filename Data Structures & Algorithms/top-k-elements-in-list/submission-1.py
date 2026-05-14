class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = {}
        #max_freq = [0]*k

        for i in nums:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1   

        freq = sorted(list(freqs.values()))[-k:]    

        for i in freqs.keys():
            if freqs[i] in freq:
                res.append(i)

        return res          

