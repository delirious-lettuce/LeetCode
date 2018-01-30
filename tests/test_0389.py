import pytest

from problems.problem_0389 import Solution


@pytest.mark.parametrize('test_input, expected', (
    (('a', 'aa'), 'a'),
    (('abcd', 'abcde'), 'e')
))
def test_find_the_difference(test_input, expected):
    assert Solution.findTheDifference(*test_input) == expected
