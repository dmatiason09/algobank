import pytest
from searching.linear_search import linear_search
from searching.binary_search import binary_search, binary_search_recursive
from searching.jump_search import jump_search
from searching.interpolation_search import interpolation_search


# these all need sorted input
SORTED_SEARCH_FNS = [
    binary_search,
    binary_search_recursive,
    jump_search,
    interpolation_search,
]


class TestLinearSearch:
    def test_finds_element(self):
        assert linear_search([4, 2, 7, 1, 9], 7) == 2

    def test_first_occurrence(self):
        assert linear_search([1, 3, 3, 5], 3) == 1

    def test_not_found(self):
        assert linear_search([1, 2, 3], 10) == -1

    def test_empty_array(self):
        assert linear_search([], 5) == -1

    def test_single_element_found(self):
        assert linear_search([42], 42) == 0

    def test_single_element_not_found(self):
        assert linear_search([42], 99) == -1

    def test_target_at_end(self):
        assert linear_search([1, 2, 3, 4, 5], 5) == 4

    def test_works_with_strings(self):
        assert linear_search(["a", "b", "c"], "b") == 1


class TestSortedSearchAlgorithms:
    """Common tests for all search functions that require sorted input."""

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_finds_element(self, search_fn):
        arr = [1, 3, 5, 7, 9, 11, 13]
        assert search_fn(arr, 7) == 3

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_finds_first_element(self, search_fn):
        arr = [2, 4, 6, 8, 10]
        assert search_fn(arr, 2) == 0

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_finds_last_element(self, search_fn):
        arr = [2, 4, 6, 8, 10]
        assert search_fn(arr, 10) == 4

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_not_found(self, search_fn):
        arr = [1, 3, 5, 7, 9]
        assert search_fn(arr, 6) == -1

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_empty_array(self, search_fn):
        assert search_fn([], 1) == -1

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_single_element_found(self, search_fn):
        assert search_fn([5], 5) == 0

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_single_element_not_found(self, search_fn):
        assert search_fn([5], 3) == -1

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_two_elements(self, search_fn):
        assert search_fn([1, 2], 1) == 0
        assert search_fn([1, 2], 2) == 1

    @pytest.mark.parametrize("search_fn", SORTED_SEARCH_FNS)
    def test_larger_array(self, search_fn):
        arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        assert search_fn(arr, 50) == 25
        assert search_fn(arr, 51) == -1
