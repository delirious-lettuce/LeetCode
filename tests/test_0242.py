import pytest

from problems.problem_0242 import Solution


@pytest.mark.parametrize('test_input, expected', (
    (('anagram', 'nagaram'), True),
    (('rat', 'car'), False),
))
def test_is_anagram(test_input, expected):
    assert Solution.isAnagram(*test_input) == expected
