# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.score

    def comparator(a, b):
        result =  b.__repr__() - a.__repr__()
        if result == 0:
            if b.name < a.name:
                result = 1
            elif b.name > a.name:
                result = -1
            else:
                result = 0
        return result

