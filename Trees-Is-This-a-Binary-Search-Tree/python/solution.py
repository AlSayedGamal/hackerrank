""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def inordered(root):
    ordered = []
    if root.left:
        ordered += inordered(root.left)
    ordered.append(root.data)
    if root.right:
        ordered += inordered(root.right)
    return ordered

def checkBST(root):
    ordered_nodes = inordered(root)
    if sorted(set(ordered_nodes)) == ordered_nodes:
        return True
    else:
        return False
