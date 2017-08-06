def array_left_rotation(a, n, k):
    original = a
    answer = a + []
    for i in range(0,n):
        answer[i-k] = original[i]
    return answer


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
