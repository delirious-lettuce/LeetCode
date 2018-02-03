import pytest

from problems.problem_0520 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ('USA', True),
    ('leetcode', True),
    ('Google', True),
))
def test_detect_capital_use(test_input, expected):
    assert Solution.detectCapitalUse(test_input) == expected
