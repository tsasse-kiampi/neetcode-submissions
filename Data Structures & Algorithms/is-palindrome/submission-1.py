class Solution:
    def isAlnum(self, s):
        return ((ord("A") <= ord(s) <= ord("Z")) or (ord("a") <= ord(s) <= ord("z")) or (ord("0") <= ord(s) <= ord("9")))

    def isPalindrome(self, s: str) -> bool:
        pal = ''.join(i for i in s if self.isAlnum(i)).lower()

        return pal == pal[::-1]

        