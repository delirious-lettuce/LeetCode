class Solution:
    """
    https://leetcode.com/problems/valid-anagram/

    Given two strings s and t, write a function to determine if t is an
      anagram of s.

    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.

    Note:
      You may assume the string contains only lowercase alphabets.

    Follow up:
      What if the inputs contain unicode characters? How would you
        adapt your solution to such case?
    """

    @staticmethod
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # # Version 1
        # return sorted(s) == sorted(t)

        # # Version 2
        # from collections import Counter
        #
        # return Counter(s) == Counter(t)

        # Version 3 -> 59ms -> beats 96.97% of Python submissions
        result = [0] * 123
        for a in s:
            result[ord(a)] += 1
        for b in t:
            result[ord(b)] -= 1
        return all(c == 0 for c in result)
