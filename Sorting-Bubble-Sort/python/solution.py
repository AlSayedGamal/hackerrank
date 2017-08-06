n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

sorted = False
swaps_count = 0
while not sorted:
    sorted = True
    for i in xrange(1,len(a)):
        if a[i-1] > a[i]:
            a[i-1], a[i] = a[i], a[i-1]
            swaps_count += 1
            sorted = False
first_element = a[0]
last_element = a[-1]

print "Array is sorted in %s swaps." % swaps_count
print "First Element: %s" % first_element
print "Last Element: %s" % last_element


