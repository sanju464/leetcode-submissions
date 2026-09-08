class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []

        for _ in range(k):
            most = max(count, key=count.get)
            result.append(most)
            del count[most]

        return result