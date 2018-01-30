import pytest

from problems.problem_0283 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([0, 1, 2], [1, 2, 0]),
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
))
def test_move_zeroes(test_input, expected):
    original_test_input_id = id(test_input)
    Solution.moveZeroes(test_input)  # sort in-place
    assert test_input == expected
    assert id(test_input) == original_test_input_id
