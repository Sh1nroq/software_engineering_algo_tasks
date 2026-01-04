import pytest
from tasks.recursion.binary_search.solution import solution, binary_search

def test_solution_is_callable():
    """Базовая проверка структуры"""
    assert callable(solution)

def test_basic_present():
    arr = [1, 2, 2, 4, 7]
    # Бинарный поиск может вернуть любой из индексов дубликатов
    assert binary_search(arr, 2) in (1, 2)
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 7) == 4

def test_not_present():
    assert binary_search([1, 3, 5], 2) == -1
    assert binary_search([], 10) == -1
    assert binary_search([5], 1) == -1

def test_edge_values():
    arr = [-10**9, -5, 0, 7, 10**9]
    assert binary_search(arr, -10**9) == 0
    assert binary_search(arr, 10**9) == 4
    assert binary_search(arr, 0) == 2

def test_single_element():
    arr = [42]
    assert binary_search(arr, 42) == 0
    assert binary_search(arr, -1) == -1

def test_large_dataset_complexity():
    # Проверяем корректность на большом массиве
    arr = list(range(1_000_000))
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 999_999) == 999_999
    assert binary_search(arr, 500_000) == 500_000
    assert binary_search(arr, 1_000_001) == -1