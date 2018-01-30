class Solution:
    """
    https://leetcode.com/problems/single-number/

    Given an array of integers, every element appears twice except for
      one. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you
      implement it without using extra memory?
    """

    @staticmethod
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        for num in nums:
            result ^= num
        return result

        # above code seems to be faster than using reduce
        # return functools.reduce(lambda a, b: a ^ b, nums)
        # return functools.reduce(operator.xor, nums)
