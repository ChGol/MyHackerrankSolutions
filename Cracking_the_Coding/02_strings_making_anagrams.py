def number_needed(a0, b0):
    list_a = [0 for x in xrange(26)]
    list_b = [0 for x in xrange(26)]
    for x in a0:
        list_a[ord(x) - 97] += 1
    for y in b0:
        list_b[ord(y) - 97] += 1
    counter = 0
    for z in range(0, 26):
        counter = counter + abs(list_a[z] - list_b[z])
    return counter


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
