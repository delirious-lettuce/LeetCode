import pytest

from problems.problem_0268 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([0], 1),
    ([0, 1], 2),
    ([1, 0], 2),
    ([1, 2, 3], 0),
    ([3, 0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
))
def test_missing_number(test_input, expected):
    assert Solution.missingNumber(test_input) == expected
