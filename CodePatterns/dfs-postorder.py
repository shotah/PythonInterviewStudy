# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

# Algorithm Postorder(tree)

# Traverse the left subtree, i.e., call Postorder(left->subtree)
# Traverse the right subtree, i.e., call Postorder(right->subtree)
# Visit the root

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A function to do postorder tree traversal
def printPostorder(root):
	if root:
		# First recur on left child
		printPostorder(root.left)
		# the recur on right child
		printPostorder(root.right)
		# now print the data of node
		print(root.val),


# Driver code
if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)

# Function call
print("\nPostorder traversal of binary tree is")
printPostorder(root)
