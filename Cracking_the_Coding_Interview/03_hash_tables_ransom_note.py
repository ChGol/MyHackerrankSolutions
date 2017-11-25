def ransom_note(magazine, ransom):
    if n > m:
        return False
    dict1 = {}
    for x in magazine:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    dict2 = {}
    for y in ransom:
        if y in dict2:
            dict2[y] += 1
        else:
            dict2[y] = 1
    for word in dict2:
        if word not in dict1:
            return False
        if dict2[word] > dict1[word]:
            return False
    return True


m, n = map(int, raw_input().strip().split(' '))
input_magazine = raw_input().strip().split(' ')
input_ransom = raw_input().strip().split(' ')
answer = ransom_note(input_magazine, input_ransom)
if answer:
    print "Yes"
else:
    print "No"
