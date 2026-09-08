class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0

        for i in range(len(s)):
            current = ""

            for j in range(i, len(s)):
                if s[j] in current:
                    break

                current += s[j]
                longest = max(longest, len(current))

        return longest

        