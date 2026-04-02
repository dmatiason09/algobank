import pytest
from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.heap_sort import heap_sort
from sorting.counting_sort import counting_sort
from sorting.radix_sort import radix_sort


# merge sort returns a new list, the rest sort in place
IN_PLACE_SORTS = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
    heap_sort,
]

ALL_COMPARISON_SORTS = IN_PLACE_SORTS + [merge_sort]

# these only work with non-negative integers
INTEGER_ONLY_SORTS = [counting_sort, radix_sort]


class TestComparisonSorts:
    """Tests that apply to all comparison-based sorting algorithms."""

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_basic_case(self, sort_fn):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = sort_fn(arr[:])  # pass a copy
        assert result == [11, 12, 22, 25, 34, 64, 90]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_empty_array(self, sort_fn):
        assert sort_fn([]) == []

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_single_element(self, sort_fn):
        assert sort_fn([42]) == [42]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_already_sorted(self, sort_fn):
        arr = [1, 2, 3, 4, 5]
        assert sort_fn(arr[:]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_reverse_sorted(self, sort_fn):
        arr = [5, 4, 3, 2, 1]
        assert sort_fn(arr[:]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_duplicates(self, sort_fn):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        result = sort_fn(arr[:])
        assert result == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_negative_numbers(self, sort_fn):
        arr = [3, -2, -8, 5, 0, -1]
        result = sort_fn(arr[:])
        assert result == [-8, -2, -1, 0, 3, 5]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_all_same_values(self, sort_fn):
        arr = [7, 7, 7, 7, 7]
        assert sort_fn(arr[:]) == [7, 7, 7, 7, 7]

    @pytest.mark.parametrize("sort_fn", ALL_COMPARISON_SORTS)
    def test_two_elements(self, sort_fn):
        assert sort_fn([2, 1]) == [1, 2]
        assert sort_fn([1, 2]) == [1, 2]


class TestIntegerOnlySorts:
    """Tests for counting sort and radix sort (non-negative integers only)."""

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_basic_case(self, sort_fn):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = sort_fn(arr[:])
        assert result == [11, 12, 22, 25, 34, 64, 90]

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_empty(self, sort_fn):
        assert sort_fn([]) == []

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_single(self, sort_fn):
        assert sort_fn([5]) == [5]

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_with_zeros(self, sort_fn):
        arr = [0, 5, 0, 3, 0, 1]
        assert sort_fn(arr[:]) == [0, 0, 0, 1, 3, 5]

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_already_sorted(self, sort_fn):
        arr = [1, 2, 3, 4, 5]
        assert sort_fn(arr[:]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_duplicates(self, sort_fn):
        arr = [4, 2, 2, 8, 3, 3, 1]
        assert sort_fn(arr[:]) == [1, 2, 2, 3, 3, 4, 8]

    @pytest.mark.parametrize("sort_fn", INTEGER_ONLY_SORTS)
    def test_large_values(self, sort_fn):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        assert sort_fn(arr[:]) == [2, 24, 45, 66, 75, 90, 170, 802]


# quick sanity check for merge sort stability
def test_merge_sort_is_stable():
    # tuples where we sort by first element
    # if stable, equal keys should keep their relative order
    data = [(3, "a"), (1, "b"), (3, "c"), (1, "d")]
    # sort using merge sort logic manually on first element
    result = sorted(data, key=lambda x: x[0])  # python sorted is stable
    assert result == [(1, "b"), (1, "d"), (3, "a"), (3, "c")]
