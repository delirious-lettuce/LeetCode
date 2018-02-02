import pytest

from problems.problem_0412 import Solution


@pytest.mark.parametrize('test_input, expected', (
    (5, ['1', '2', 'Fizz', '4', 'Buzz']),
    (10, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8',
          'Fizz', 'Buzz']),
    (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8',
          'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
))
def test_fizz_buzz(test_input, expected):
    assert Solution.fizzBuzz(test_input) == expected
