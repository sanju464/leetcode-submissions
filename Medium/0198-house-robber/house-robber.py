class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_two = 0
        previous_one = 0

        for money in nums:
            current = max(
                previous_one,
                previous_two + money
            )

            previous_two = previous_one
            previous_one = current

        return previous_one