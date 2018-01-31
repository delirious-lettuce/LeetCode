class Solution:
    """
    https://leetcode.com/problems/contains-duplicate/

    Given an array of integers, find if the array contains any
      duplicates. Your function should return true if any value appears
      at least twice in the array, and it should return false if every
      element is distinct.
    """

    @staticmethod
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
