class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # edge case
        if len(nums) == 0:
            return 0

        # write pointer (position of next unique element)
        write = 1

        # read pointer
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write