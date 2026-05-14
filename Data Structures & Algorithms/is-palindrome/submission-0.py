class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ''.join(i for i in s if i.isalnum()).lower()

        return pal == pal[::-1]

        