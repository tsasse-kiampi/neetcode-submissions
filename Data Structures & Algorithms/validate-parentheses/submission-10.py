class Solution:
    def isValid(self, s: str) -> bool:

        match = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for i in s:
            if i not in match:
                stack.append(i)
            elif i in match and not stack:
                return False
            elif i in match and match[i] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False            


                    



        

        