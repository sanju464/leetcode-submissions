class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        rev = ""

        for i in range(len(s) - 1, -1, -1):
            rev += s[i]

        return s == rev