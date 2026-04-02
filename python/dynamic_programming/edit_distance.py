"""
Edit Distance (Levenshtein Distance)
-------------------------------------
Time:  O(m * n)
Space: O(m * n), or O(min(m, n)) optimized

Minimum number of operations (insert, delete, replace) to transform
one string into another.

Used a lot in spell checkers, DNA sequence alignment, diff tools.
"""


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base cases: transforming empty string to/from something
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete
                    dp[i][j - 1],      # insert
                    dp[i - 1][j - 1],  # replace
                )

    return dp[m][n]
