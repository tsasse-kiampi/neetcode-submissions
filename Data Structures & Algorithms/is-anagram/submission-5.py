class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        occur1 = {}
        occur2 = {}

        for c in s:
            if c in occur1:
                occur1[c] += 1
            else:
                occur1[c] = 1     

        for c in t:
            if c in occur2:
                occur2[c] += 1
            else:
                occur2[c] = 1   

        return occur1 == occur2     
        