class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        corr = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in corr:
                if stack and corr[c] == stack[-1]:
                    stack.pop()
                else: return False
            else:
                stack.append(c)

        return True if not stack else False        





        

        




        

        