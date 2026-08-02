class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = -int(str(-x)[::-1])
        else:
            rev = int(str(x)[::-1])

        if rev < -2147483648 or rev > 2147483647:
            return 0

        return rev