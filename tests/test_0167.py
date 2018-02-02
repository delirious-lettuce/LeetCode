import pytest

from problems.problem_0167 import Solution


@pytest.mark.parametrize('test_input, expected', (
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3])
))
def test_two_sum(test_input, expected):
    assert Solution.twoSum(*test_input) == expected
