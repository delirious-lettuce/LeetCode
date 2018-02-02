import pytest

from problems.problem_0485 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([1, 1, 0, 1, 1, 1], 3),
    ([1, 1, 0, 1], 2),
    ([], 0),
))
def test_find_max_consecutive_ones(test_input, expected):
    assert Solution.findMaxConsecutiveOnes(test_input) == expected
