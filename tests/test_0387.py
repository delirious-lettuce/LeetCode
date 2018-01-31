import pytest

from problems.problem_0387 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ('leetcode', 0),
    ('loveleetcode', 2),
))
def test_first_uniq_char(test_input, expected):
    assert Solution.firstUniqChar(test_input) == expected
