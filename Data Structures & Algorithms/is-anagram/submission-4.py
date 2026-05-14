class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        occur1 = {}
        occur2 = {}

        for c in s:
            occur1[c] = 1 + occur1.get(c, 0) 

        for c in t:
            occur2[c] = 1 + occur2.get(c, 0)   

        return occur1 == occur2     
        