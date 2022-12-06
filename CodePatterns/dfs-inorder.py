# Python3 program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree

# Traverse the left subtree, i.e., call Inorder(left->subtree)
# Visit the root.
# Traverse the right subtree, i.e., call Inorder(right->subtree)
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.val),
        # now recur on right child
        printInorder(root.right)
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("\nInorder traversal of binary tree is")
    printInorder(root)
