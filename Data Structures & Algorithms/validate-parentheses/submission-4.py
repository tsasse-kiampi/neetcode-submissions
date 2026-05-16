class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in [")", "}", "]"] or len(s)%2 != 0: return False

        match = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for i in range(len(s)):
            if s[i] not in match:
                stack.append(s[i])
            elif s[i] in match and len(stack) == 0:
                return False
            elif s[i] in match and match[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0            


                    



        

        