from itertools import zip_longest

class Solution(object):
    """
    https://leetcode.com/problems/add-strings/

    Given two non-negative integers num1 and num2 represented as
      string, return the sum of num1 and num2.

    Note:

      1. The length of both num1 and num2 is < 5100.
      2. Both num1 and num2 contains only digits 0-9.
      3. Both num1 and num2 does not contain any leading zero.
      4. You must not use any built-in BigInteger library or convert
           the inputs to integer directly.
    """

    @staticmethod
    def addStrings(num_1, num_2):
        """
        :type num_1: str
        :type num_2: str
        :rtype: str

        Version 1: 52ms (benchmark time only, no converting to int)
        Version 2: 66ms
        """

        # # Version 1
        # return str(int(num_1) + int(num_2))

        # Version 2
        carry = 0
        result = []
        for a, b in zip_longest(reversed(num_1),
                                reversed(num_2),
                                fillvalue='0'):
            carry, rem = divmod(ord(a) + ord(b) - 96 + carry, 10)
            result.append(str(rem))

        if carry != 0:
            result.append(str(carry))
        return ''.join(reversed(result))
