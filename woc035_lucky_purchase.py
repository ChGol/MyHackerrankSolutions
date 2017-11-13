#!/bin/python

import sys

if __name__ == "__main__":
    my_dict = {}
    actual_min_price = sys.maxint
    name = ''
    n = int(raw_input().strip())
    for a0 in xrange(n):
        s, n = raw_input().strip().split(' ')
        s, n = [str(s), int(n)]
        number = str(n)
        n_4 = 0
        n_7 = 0
        no_other_digits = True
        for x in number:
            if x == '4':
                n_4 += 1
            elif x == '7':
                n_7 += 1
            else:
                no_other_digits = False
                break
        if n_4 == n_7 and n_4 != 0 and n_7 != 0 and no_other_digits:
            my_dict[s] = n
            if n < actual_min_price:
                actual_min_price = n
                name = s
    if not my_dict:
        print '-1'
    else:
        print name
