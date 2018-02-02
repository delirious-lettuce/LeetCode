import pytest

from problems.problem_0557 import Solution


@pytest.mark.parametrize('test_input, expected', (
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("Another test string!", "rehtonA tset !gnirts")
))
def test_reverse_words(test_input, expected):
    assert Solution.reverseWords(test_input) == expected
