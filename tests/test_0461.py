import pytest

from problems import problem_0461


@pytest.fixture(scope='module')
def solution():
    return problem_0461.Solution()


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ((1, 4), 2),
        ((142, 77), 4),
        ((13435, 98237), 9)
    )
)
def test_hamming_distance(test_input, expected, solution):
    assert solution.hammingDistance(*test_input) == expected
