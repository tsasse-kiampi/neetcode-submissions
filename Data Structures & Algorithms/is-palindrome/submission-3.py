class Solution:
    def isPalindrome(self, s: str) -> bool:
        msg = "".join(i.lower() for i in s if (i.isalpha() or i.isdigit()))
        return msg == msg[::-1]
        