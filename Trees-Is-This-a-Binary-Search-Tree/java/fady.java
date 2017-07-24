/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }return true;
*/

boolean go(Node root, int min, int max) {
    if(root == null) return true;
    else if(root.data > max || root.data < min) return false;
    else { return (go(root.left, min, root.data-1) && go(root.right, root.data+1, max)); }
}

boolean checkBST(Node root) {
    return go(root, 0, 1000000000);
}
