#!/bin/python

import sys


def matrix_land(a):
    max_sum_right = [0 for x in xrange(m)]
    msr = [0 for x in xrange(m)]
    d = [0 for x in xrange(m)]
    dp = [row[:] for row in a]

    for i in xrange(1, n):
        for j in xrange(1, m):
            max_sum_right[j] = max(max_sum_right[j - 1] + a[i][j], 0)
        for j in xrange(m, 0, -1):
            msr[j] = max(msr[j + 1] + a[i][j], 0)

        d[1] = dp[i - 1][1] + a[i][1]
        dp[i][1] = d[1] + msr[2]
        for j in xrange(2, m):
            d[j] = max(d[j - 1] + a[i][j], dp[i - 1][j] + a[i][j] + max_sum_right[j - 1])
            dp[i][j] = d[j] + msr[j + 1]

        d[m] = dp[i - 1][m] + a[i][m]
        dp[i][m] = max(dp[i][m], d[m] + max_sum_right[m - 1])
        for j in xrange(m - 1, 0, -1):
            d[j] = max(d[j + 1] + a[i][j], dp[i - 1][j] + a[i][j] + msr[j + 1])
            dp[i][j] = max(dp[i][j], d[j] + max_sum_right[j - 1])

    ans = dp[n][1]
    for i in xrange(2, m):
        ans = max(ans, dp[n][i])

    return ans


if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = []
    for A_i in xrange(n):
        A_temp = map(int, raw_input().strip().split(' '))
        A.append(A_temp)
    result = matrix_land(A)
    print result
