import pytest
from dynamic_programming.fibonacci import fib_naive, fib_memo, fib_bottom_up
from dynamic_programming.knapsack import knapsack, knapsack_optimized
from dynamic_programming.lcs import lcs_length, lcs
from dynamic_programming.lis import lis_dp, lis_binary_search
from dynamic_programming.coin_change import coin_change, coin_change_ways
from dynamic_programming.edit_distance import edit_distance
from dynamic_programming.max_subarray import max_subarray, max_subarray_with_indices
from dynamic_programming.climbing_stairs import climb_stairs, climb_stairs_k_steps
from dynamic_programming.unique_paths import unique_paths, unique_paths_with_obstacles


class TestFibonacci:
    @pytest.mark.parametrize("fib_fn", [fib_naive, fib_memo, fib_bottom_up])
    def test_base_cases(self, fib_fn):
        assert fib_fn(0) == 0
        assert fib_fn(1) == 1

    @pytest.mark.parametrize("fib_fn", [fib_naive, fib_memo, fib_bottom_up])
    def test_known_values(self, fib_fn):
        assert fib_fn(5) == 5
        assert fib_fn(10) == 55

    def test_memo_handles_large_n(self):
        assert fib_memo(100) == 354224848179261915075

    def test_bottom_up_handles_large_n(self):
        assert fib_bottom_up(100) == 354224848179261915075


class TestKnapsack:
    def test_basic(self):
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        assert knapsack(weights, values, 7) == 9  # items 2 and 3

    def test_optimized_matches(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        cap = 8
        assert knapsack(weights, values, cap) == knapsack_optimized(weights, values, cap)

    def test_zero_capacity(self):
        assert knapsack([1, 2], [10, 20], 0) == 0

    def test_empty_items(self):
        assert knapsack([], [], 10) == 0

    def test_single_item_fits(self):
        assert knapsack([5], [10], 5) == 10

    def test_single_item_doesnt_fit(self):
        assert knapsack([5], [10], 3) == 0


class TestLCS:
    def test_basic(self):
        assert lcs_length("abcde", "ace") == 3
        assert lcs("abcde", "ace") == "ace"

    def test_no_common(self):
        assert lcs_length("abc", "xyz") == 0
        assert lcs("abc", "xyz") == ""

    def test_identical(self):
        assert lcs_length("hello", "hello") == 5
        assert lcs("hello", "hello") == "hello"

    def test_one_empty(self):
        assert lcs_length("abc", "") == 0
        assert lcs_length("", "abc") == 0

    def test_subsequence_not_substring(self):
        # "ac" is a subsequence but not a substring of "abc"
        assert lcs_length("abc", "ac") == 2


class TestLIS:
    @pytest.mark.parametrize("lis_fn", [lis_dp, lis_binary_search])
    def test_basic(self, lis_fn):
        assert lis_fn([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    @pytest.mark.parametrize("lis_fn", [lis_dp, lis_binary_search])
    def test_all_increasing(self, lis_fn):
        assert lis_fn([1, 2, 3, 4, 5]) == 5

    @pytest.mark.parametrize("lis_fn", [lis_dp, lis_binary_search])
    def test_all_decreasing(self, lis_fn):
        assert lis_fn([5, 4, 3, 2, 1]) == 1

    @pytest.mark.parametrize("lis_fn", [lis_dp, lis_binary_search])
    def test_empty(self, lis_fn):
        assert lis_fn([]) == 0

    @pytest.mark.parametrize("lis_fn", [lis_dp, lis_binary_search])
    def test_single_element(self, lis_fn):
        assert lis_fn([7]) == 1


class TestCoinChange:
    def test_basic(self):
        assert coin_change([1, 5, 10, 25], 30) == 2  # 25 + 5

    def test_impossible(self):
        assert coin_change([2], 3) == -1

    def test_zero_amount(self):
        assert coin_change([1, 2, 5], 0) == 0

    def test_single_coin(self):
        assert coin_change([3], 9) == 3

    def test_ways_basic(self):
        assert coin_change_ways([1, 2, 5], 5) == 4

    def test_ways_single_denomination(self):
        assert coin_change_ways([2], 6) == 1  # only one way: 2+2+2

    def test_ways_zero(self):
        assert coin_change_ways([1, 2], 0) == 1  # one way: use nothing


class TestEditDistance:
    def test_basic(self):
        assert edit_distance("kitten", "sitting") == 3

    def test_same_strings(self):
        assert edit_distance("hello", "hello") == 0

    def test_empty_to_something(self):
        assert edit_distance("", "abc") == 3

    def test_something_to_empty(self):
        assert edit_distance("abc", "") == 3

    def test_both_empty(self):
        assert edit_distance("", "") == 0

    def test_single_char_diff(self):
        assert edit_distance("a", "b") == 1


class TestMaxSubarray:
    def test_basic(self):
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_positive(self):
        assert max_subarray([1, 2, 3, 4]) == 10

    def test_all_negative(self):
        assert max_subarray([-3, -2, -5, -1]) == -1

    def test_single_element(self):
        assert max_subarray([42]) == 42

    def test_empty(self):
        assert max_subarray([]) == 0

    def test_with_indices(self):
        total, start, end = max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        assert total == 6
        assert start == 3
        assert end == 6


class TestClimbingStairs:
    def test_base_cases(self):
        assert climb_stairs(1) == 1
        assert climb_stairs(2) == 2

    def test_known_values(self):
        assert climb_stairs(3) == 3
        assert climb_stairs(5) == 8

    def test_k_steps(self):
        # with 1-3 steps, n=4: 1111, 112, 121, 211, 13, 31, 22 = 7
        assert climb_stairs_k_steps(4, 3) == 7

    def test_k_steps_equals_regular_when_k2(self):
        for n in range(1, 10):
            assert climb_stairs_k_steps(n, 2) == climb_stairs(n)


class TestUniquePaths:
    def test_basic(self):
        assert unique_paths(3, 7) == 28

    def test_single_row(self):
        assert unique_paths(1, 5) == 1

    def test_single_column(self):
        assert unique_paths(5, 1) == 1

    def test_square(self):
        assert unique_paths(3, 3) == 6

    def test_with_obstacles(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        assert unique_paths_with_obstacles(grid) == 2

    def test_blocked_start(self):
        grid = [[1, 0], [0, 0]]
        assert unique_paths_with_obstacles(grid) == 0

    def test_no_obstacles(self):
        grid = [[0, 0], [0, 0]]
        assert unique_paths_with_obstacles(grid) == 2
