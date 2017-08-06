contacts_book = {}
def add(contacts_book, contact):
    root = contacts_book
    for char in contact:
        found = root.get(char, None)
        if found:
            root[char]['count'] += 1
        else:
            root[char] = {'count':1}
        root = root[char]
    return contacts_book

def find(contacts_book, contact):
    #print contacts_book
    root = contacts_book
    for char in contact:
        found = root.get(char, None)
        if not found:
            result = 0
            break
        else:
            root = found
    else:
        result = root['count']
    return result

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add":
        add(contacts_book, contact)
    else:
        print find(contacts_book, contact)

