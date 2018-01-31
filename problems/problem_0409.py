class Solution:
    """
    https://leetcode.com/problems/longest-palindrome/

    Given a string which consists of lowercase or uppercase letters,
      find the length of the longest palindromes that can be built with
      those letters.

    This is case sensitive, for example "Aa" is not considered a
      palindrome here.

    Note:
      Assume the length of given string will not exceed 1,010.

    Example:

      Input:
      "abccccdd"

      Output:
      7

      Explanation:
        One longest palindrome that can be built is "dccaccd", whose
          length is 7.
    """

    @staticmethod
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: int
        """

        # # Version 1 -> 62ms
        # from collections import Counter
        #
        # cnt = Counter(s)
        # result = 0
        # for k, v in cnt.items():
        #     current = v / 2 * 2
        #     cnt[k] -= current
        #     result += current
        # return result + next((1 for v in cnt.values() if v == 1), 0)

        # # Version 2 -> 62ms
        # counts = [0] * 123
        # result = 0
        # for a in s:
        #     counts[ord(a)] += 1
        #
        # for i, b in enumerate(counts):
        #     current = b / 2 * 2
        #     counts[i] -= current
        #     result += current
        #
        # return result + next((1 for c in counts if c == 1), 0)

        # Version 3 -> 59ms
        result = 0
        seen = set()
        for char in s:
            if char in seen:
                result += 2
                seen.remove(char)
            else:
                seen.add(char)
        return result + bool(seen)
