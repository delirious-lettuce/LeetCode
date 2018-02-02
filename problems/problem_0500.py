import re


class Solution:
    """
    https://leetcode.com/problems/keyboard-row/

    Given a List of words, return the words that can be typed using
      letters of alphabet on only one row's of American keyboard like
      the image below.

    Example 1:
      Input: ["Hello", "Alaska", "Dad", "Peace"]
      Output: ["Alaska", "Dad"]

    Note:
      1. You may use one character in the keyboard more than once.
      2. You may assume the input string will only contain letters of
           alphabet.
    """

    @staticmethod
    def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # # Version 1
        # rows = (set('qwertyuiopQWERTYUIOP'),
        #         set('asdfghjklASDFGHJKL'),
        #         set('zxcvbnmZXCVBNM'))
        # return [word for word in words
        #         if any(row.issuperset(word) for row in rows)]

        # Version 2
        regex = re.compile(
            r'([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$', re.IGNORECASE
        )
        return [word for word in words if regex.match(word)]
