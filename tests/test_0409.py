import pytest

from problems.problem_0409 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ('abccccdd', 7),
    ('aaabbbccc', 7),
    ('ccc', 3),
    ('ccd', 3),
    ('bb', 2)
))
def test_longest_palindrome(test_input, expected):
    assert Solution.longestPalindrome(test_input) == expected
