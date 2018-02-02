import pytest

from problems.problem_0500 import Solution


@pytest.mark.parametrize('test_input, expected', (
    (['Hello', 'Alaska', 'Dad', 'Peace'], ['Alaska', 'Dad']),
    (['Toy', 'Flask', 'BMX'], ['Toy', 'Flask', 'BMX']),
    (['LeetCode', 'Algorithms'], []),
))
def test_find_words(test_input, expected):
    assert Solution.findWords(test_input) == expected
