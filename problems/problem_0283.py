class Solution:
    """
    https://leetcode.com/problems/move-zeroes/

    Given an array nums, write a function to move all 0's to the end of
      it while maintaining the relative order of the non-zero elements.

    For example, given nums = [0, 1, 0, 3, 12], after calling your
      function, nums should be [1, 3, 12, 0, 0].

    Note:
      1. You must do this in-place without making a copy of the array.
      2. Minimize the total number of operations.
    """

    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place.
        """

        # nums.sort(key=lambda a: a == 0)

        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero_pos != i:
                    nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
