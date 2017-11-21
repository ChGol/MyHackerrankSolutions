def array_left_rotation(a0, n0, k0):
    if k0 < n0:
        temp_list = a0[:k0]
        a0 = a0[k0:] + temp_list
    else:
        for x in range(0, k0):
            temp_list = [a0[0]]
            a0 = a0[1:] + temp_list
    return a0


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str, answer))
