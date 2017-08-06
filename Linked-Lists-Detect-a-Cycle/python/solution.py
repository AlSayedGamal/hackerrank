"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    visited = {}
    visited[head] = True
    cycle = False
    if head is not None:
        next_node = head.next
        if next_node == head or visited.get(next_node, False):
            cycle = True
        else:
            visited[next_node] = True
            cycle = has_cycle(next_node)
    return cycle

