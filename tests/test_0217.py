import pytest

from problems.problem_0217 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ([1, 2, 3], False),
    ([1, 2, 3, 1], True),
    (list(range(1000)) + [999], True)
))
def test_contains_duplicate(test_input, expected):
    assert Solution.containsDuplicate(test_input) == expected
