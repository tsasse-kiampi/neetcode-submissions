class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurS, occurT = {}, {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            occurS[s[i]] =  1 + occurS.get(s[i], 0)
            occurT[t[i]] =  1 + occurT.get(t[i], 0)

        return occurS == occurT    


                         

        