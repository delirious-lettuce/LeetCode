class Solution:
    """
    https://leetcode.com/problems/first-unique-character-in-a-string/

    Given a string, find the first non-repeating character in it and
      return it's index. If it doesn't exist, return -1.

    Examples:

      s = "leetcode"
      return 0

      s = "loveleetcode",
      return 2

    Note:
      You may assume the string contain only lowercase letters.
    """

    @staticmethod
    def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """

        # # Version 1
        # # using collections.Counter is slower
        # from collections import Counter
        #
        # cnt = Counter(s)
        # return next((i for i, a in enumerate(s) if cnt[a] == 1), -1)

        # Version 2
        frequency = [0] * 123
        for a in s:
            frequency[ord(a)] += 1
        return next((i for i, b in enumerate(s) if frequency[ord(b)] == 1), -1)
