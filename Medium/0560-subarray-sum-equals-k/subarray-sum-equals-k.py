class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        seen = {0: 1}

        for num in nums:
            total += num

            if total - k in seen:
                count += seen[total - k]

            seen[total] = seen.get(total, 0) + 1

        return count