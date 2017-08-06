def number_needed(a, b):
    look_up = {}
    count = 0
    for i in a:
        char_found = look_up.get(i, False)
        if char_found:
            look_up[i] += 1
        else:
            look_up[i] = 1
    for j in b:
        char_found = look_up.get(j, False)
        if char_found:
            look_up[j] -= 1
        else:
            look_up[j] = -1
    for c in look_up.keys():
        count += abs(look_up[c])

    return count



a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
