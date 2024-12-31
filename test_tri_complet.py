
from random import randint, sample
import pytest
from tri import tri_selection, tri_bulle, tri_insertion, quicksort

def is_sorted(arr):
    return arr == sorted(arr)

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_empty_array(sort_func):
    assert is_sorted(sort_func([])) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_single_element_array(sort_func):
    assert is_sorted(sort_func([5])) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_array_with_duplicates(sort_func):
    assert is_sorted(sort_func([4, 2, 2, 4, 1, 5])) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_string_array(sort_func):
    assert is_sorted(sort_func(["apple", "banana", "cherry", "date", "apple"])) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_smallest_at_end(sort_func):
    assert is_sorted(sort_func([3, 4, 5, 6, 1])) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_random_array(sort_func):
    random_array = [randint(0, 100) for _ in range(10)]
    assert is_sorted(sort_func(random_array)) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_large_array(sort_func):
    large_array = sample(range(10000), 1000)
    assert is_sorted(sort_func(large_array)) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_sorted_array(sort_func):
    sorted_array = [1, 2, 3, 4, 5]
    assert is_sorted(sort_func(sorted_array)) == True

@pytest.mark.parametrize("sort_func", [tri_selection, tri_bulle, tri_insertion, quicksort])
def test_reverse_sorted_array(sort_func):
    reverse_sorted_array = [5, 4, 3, 2, 1]
    assert is_sorted(sort_func(reverse_sorted_array)) == True
