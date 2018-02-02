import pytest

from problems.problem_0169 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([1, 2, 2], 2),
    ([1, 1, 1, 2, 2], 1),
    ([1, 2, 3, 2, 2, 2], 2),
    ([3, 2, 1, 3, 1, 3, 3], 3)
))
def test_majority_element(test_input, expected):
    assert Solution.majorityElement(test_input) == expected
