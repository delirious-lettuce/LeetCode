from itertools import groupby


class Solution:
    """
    https://leetcode.com/problems/max-consecutive-ones/

    Given a binary array, find the maximum number of consecutive 1s in
      this array.

    Example 1:
      Input: [1,1,0,1,1,1]
      Output: 3
      Explanation:
        The first two digits or the last three digits are consecutive
          1s. The maximum number of consecutive 1s is 3.

    Note:
      1. The input array will only contain 0 and 1.
      2. The length of input array is a positive integer and will not
           exceed 10,000
    """

    @staticmethod
    def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return max(
            (sum(1 for _ in g) if k else 0 for k, g in groupby(nums)),
            default=0
        )
