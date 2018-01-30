import pytest

from problems.problem_0461 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ((1, 4), 2),
    ((142, 77), 4),
    ((13435, 98237), 9)
))
def test_hamming_distance(test_input, expected):
    assert Solution.hammingDistance(*test_input) == expected
