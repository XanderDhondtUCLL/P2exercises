import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('correct_string',[
        '',
        '()',
        '((())())',
])
def test_matching(correct_string):
    assert matching_parentheses(correct_string) == True, f'{correct_string} has matching parentheses'

@pytest.mark.parametrize('wrong_string',[
    ')',
    '(()',
    ')(()))(',
    '())'
])
def test_unmatching(wrong_string):
    assert matching_parentheses(wrong_string) == False, f'{wrong_string} does not match'