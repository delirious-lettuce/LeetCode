import pytest

from problems.problem_0463 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([[1, 1, 0],
      [0, 1, 0],
      [0, 0, 0]], 8),
    ([[0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0]], 16),
))
def test_island_perimeter(test_input, expected):
    assert Solution.islandPerimeter(test_input) == expected
