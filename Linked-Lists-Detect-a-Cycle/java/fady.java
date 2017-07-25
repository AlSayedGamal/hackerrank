/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as:
    class Node {
        int data;
        Node next;
    }
*/

boolean go(Node head, HashMap m){
    if(head==null) return false;
    else {
        if(m.containsKey(head)) return true;
        else{
            m.put(head,1);
            return go(head.next, m);
        }
    }
}

boolean hasCycle(Node head) {
    return go(head, new HashMap<Node, Integer>());
}
