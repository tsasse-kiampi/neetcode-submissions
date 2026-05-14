class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = {}
        max_freq = []

        for i in nums:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1   

        freq = list(freqs.values())
        used = [False] * len(freq)
        
        for _ in range(k):
            m = -float('inf')
            idx = -1

            for i in range(len(freq)):
                if not used[i] and freq[i] > m:
                    m = freq[i]
                    idx = i
            max_freq.append(m)
            used[idx] = True

        for i in freqs.keys():
            if freqs[i] in max_freq:
                res.append(i)    

        return res        


            

        