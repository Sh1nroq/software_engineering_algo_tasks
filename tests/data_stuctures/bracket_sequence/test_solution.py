import pytest
from tasks.data_stuctures.bracket_sequence.solution import solution

def test_solution_is_callable():
    assert callable(solution)

def test_correct_sequences():
    assert solution("{[()]}") is True
    assert solution("()[]{}") is True
    assert solution("") is True

def test_incorrect_sequences():
    assert solution("{]}") is False
    assert solution("([)]") is False
    assert solution("(((") is False
    assert solution(")") is False

def test_with_text():
    assert solution("print(arr[0])") is True
    assert solution("print(arr[0])}") is False

def test_only_closing():
    assert solution("]]]") is False

def test_only_opening():
    assert solution("(((") is False