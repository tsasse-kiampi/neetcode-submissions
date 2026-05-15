class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:    
            l = len(strs)
            msg = "-".join(i for i in strs)
            return str(l) + "-" + msg

    def decode(self, s: str) -> List[str]:
        if s == "": 
            return []

        idx = 0
        l = 0
        for i in range(len(s)):
            if s[i] == "-":
                l = int(s[0:i])
                idx = i
                break
            else:
                continue    

        if len(s) == l + 1: return [""] * (l)
        else:
            strs = []
            left,right = idx + 1, idx + 1

            while right < len(s):
                if s[right] == "-":
                    strs.append(s[left:right])
                    right += 1
                    left = right 
                else: 
                    right += 1
            strs.append(s[left:right])        
            return strs            
