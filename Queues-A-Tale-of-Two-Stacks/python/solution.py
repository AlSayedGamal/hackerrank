class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        tmp = self.pop()
        self.second.append(tmp)
        return tmp

    def pop(self):
        if len(self.second) == 0:
            #reverse first into second
            self.second = list(reversed(self.first))
            #self.first[::-1]
            self.first = []
        return self.second.pop()

    def put(self, value):
        self.first.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
