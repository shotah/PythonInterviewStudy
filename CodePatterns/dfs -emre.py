# https://emre.me/coding-patterns/depth-first-search/


# How to identify?

# This approach is quite useful when dealing with the problems 
# involving traversal of a tree.

# When the problem asks the traversal of a tree, 
# you should think about Depth First Search (DFS) 
# pattern and using it in combination with a recursive approach.


# Note: A leaf is a node with no children.

# Example:
# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which sum is 22.

# Depth First Search Solution
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val
        )

# Time Complexity: O(N) where N is the total number of nodes in the tree.

# Space Complexity: O(N), this space will be used to store the recursion stack. 
# The worst case will happen when the given tree is a linked list 
# (i.e. every node has only one child)
