class Solution:
    """
    https://leetcode.com/problems/majority-element/

    Given an array of size n, find the majority element. The majority
      element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element
      always exist in the array.
    """

    @staticmethod
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # # Version 1 -> 89 ms
        # from collections import Counter
        #
        # return Counter(nums).most_common(1)[0][0]

        # # Version 2 -> 62ms
        # majority = len(nums) // 2
        # seen = {}
        # for num in nums:
        #     try:
        #         seen[num] += 1
        #     except KeyError:
        #         seen[num] = 1
        # return next(k for k, v in seen.items() if v > majority)

        # Version 3 -> 62 ms
        count = majority = 0
        for num in nums:
            if count == 0:
                majority = num
            if majority == num:
                count += 1
            else:
                count -= 1
            # count += 1 if majority == num else -1
        return majority
