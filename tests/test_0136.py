import pytest

from problems import problem_0136


@pytest.fixture(scope='module')
def solution():
    return problem_0136.Solution()


@pytest.mark.parametrize('test_input, expected', (
    ([1], 1),
    ([1, 2, 1], 2),
    ([1, 1, 2, 2, 3], 3)
))
def test_(test_input, expected, solution):
    assert solution.singleNumber(test_input) == expected
