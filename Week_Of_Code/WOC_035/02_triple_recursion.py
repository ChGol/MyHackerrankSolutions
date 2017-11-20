#!/bin/python

import sys


def tripleRecursion(n, m, k):
    a = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                a[i][j] = m
            elif i == j:
                a[i][j] = a[i - 1][j - 1] + k
            elif i > j:
                a[i][j] = a[i - 1][j] - 1
            elif i < j:
                a[i][j] = a[i][j - 1] - 1
            print '{:1}'.format(a[i][j]),
        print


if __name__ == "__main__":
    n, m, k = raw_input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
