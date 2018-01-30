import pytest

from problems.problem_0415 import Solution


@pytest.mark.parametrize('test_input, expected', (
    (('0', '0'), '0'),
    (('123', '456'), '579'),
    (('1', '9'), '10'),
    (('9', '99'), '108')
))
def test_add_strings(test_input, expected):
    assert Solution.addStrings(*test_input) == expected
