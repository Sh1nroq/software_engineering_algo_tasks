import pytest
from tasks.data_stuctures.stack_max.solution import StackMax, solution


def test_solution_is_callable():
    assert callable(solution)


def test_basic_behavior():
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    stack.push(7)
    assert stack.get_max() == 7

    stack.push(1)
    stack.push(3)
    assert stack.get_max() == 7

    stack.pop()
    stack.pop()
    assert stack.get_max() == 7

    stack.pop()
    assert stack.get_max() == "None"


def test_increasing_sequence():
    stack = StackMax()
    for i in range(1, 6):
        stack.push(i)
        assert stack.get_max() == i

    for i in reversed(range(1, 6)):
        assert stack.get_max() == i
        stack.pop()


def test_decreasing_sequence():
    stack = StackMax()
    for x in [5, 4, 3, 2, 1]:
        stack.push(x)
        assert stack.get_max() == 5

    for _ in range(5):
        stack.pop()
    assert stack.get_max() == "None"


def test_duplicate_max_values():
    stack = StackMax()
    stack.push(10)
    stack.push(10)
    stack.push(10)
    assert stack.get_max() == 10

    stack.pop()
    assert stack.get_max() == 10
    stack.pop()
    assert stack.get_max() == 10
    stack.pop()
    assert stack.get_max() == "None"


def test_large_operations():
    stack = StackMax()
    n = 5000
    for i in range(n):
        stack.push(i)

    assert stack.get_max() == n - 1

    for i in reversed(range(n)):
        assert stack.get_max() == i
        stack.pop()

    assert stack.get_max() == "None"