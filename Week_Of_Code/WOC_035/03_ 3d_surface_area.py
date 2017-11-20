#!/bin/python

import sys


def surface_area(input_matrix_a, height, width):
    price = 0

    for row_a in input_matrix_a:
        for element_a in xrange(width):
            if element_a + 1 <= width - 1:
                price += abs(row_a[element_a] - row_a[element_a + 1])
        price += row_a[0]
        price += row_a[width - 1]

    transposed_matrix_b = zip(*input_matrix_a)
    for row_b in transposed_matrix_b:
        for element_b in xrange(height):
            if element_b + 1 <= height - 1:
                price += abs(row_b[element_b] - row_b[element_b + 1])
        price += row_b[0]
        price += row_b[height - 1]

    price += height * width * 2
    return price


if __name__ == "__main__":
    H, W = raw_input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in xrange(H):
        A_temp = map(int, raw_input().strip().split(' '))
        A.append(A_temp)
    result = surface_area(A, H, W)
    print result
