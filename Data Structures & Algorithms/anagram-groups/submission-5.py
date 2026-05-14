class Solution:

    def freq(self, s:str):
        encode_freq = [0]*26
        for i in s:
            encode_freq[ord(i) - ord('a')] += 1
        return tuple(encode_freq)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}

        for s in strs:
            if self.freq(s) not in groups.keys():
                groups[self.freq(s)] = [s]
            else:
                groups[self.freq(s)].append(s)

        for v in groups.values():
            res.append(v)

        return res              
        