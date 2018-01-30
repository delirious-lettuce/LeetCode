import pytest

from problems.problem_0136 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([1], 1),
    ([1, 2, 1], 2),
    ([1, 1, 2, 2, 3], 3)
))
def test_single_number(test_input, expected):
    assert Solution.singleNumber(test_input) == expected
