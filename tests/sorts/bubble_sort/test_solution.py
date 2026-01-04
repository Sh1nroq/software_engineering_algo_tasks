import pytest
from tasks.sorts.bubble_sort.solution import solution, bubble_sort


def test_solution_is_callable():
    assert callable(solution)


def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [[1, 2, 3, 4]]


def test_reverse_order():
    assert bubble_sort([3, 2, 1]) == [
        [2, 1, 3],
        [1, 2, 3],
    ]


def test_with_duplicates():
    assert bubble_sort([3, 3, 1]) == [
        [3, 1, 3],
        [1, 3, 3],
    ]


def test_negative_values():
    assert bubble_sort([7, -2, -1]) == [
        [-2, -1, 7],
    ]


def test_large_behavior_complexity():
    arr = list(range(100, 0, -1))
    snaps = bubble_sort(arr)

    assert len(snaps) == 99
    assert snaps[-1] == sorted(arr)
    assert snaps[0][-1] == 100