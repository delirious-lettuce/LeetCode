class Solution:
    """
    https://leetcode.com/problems/fizz-buzz/

    Write a program that outputs the string representation of numbers
      from 1 to n.

    But for multiples of three it should output “Fizz” instead of the
      number and for the multiples of five output “Buzz”. For numbers
      which are multiples of both three and five output “FizzBuzz”.

    Example:

      n = 15,

      Return:
      [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
      ]
    """

    @staticmethod
    def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        for a in range(1, n + 1):
            current = []
            if not a % 3:
                current.append('Fizz')
            if not a % 5:
                current.append('Buzz')
            result.append(''.join(current) or str(a))
        return result
