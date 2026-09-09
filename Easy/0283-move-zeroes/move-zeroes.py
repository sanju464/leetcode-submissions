class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1

        while write < len(nums):
            nums[write] = 0
            write += 1

        