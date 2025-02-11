# https://emre.me/coding-patterns/breadth-first-search/

# How to identify?

# This approach is quite useful when dealing with the problems 
# involving traversal of a tree in a level-by-level order.

# When the problem asks the traversal of a tree, 
# you should think about Breadth First Search (BFS) 
# pattern and using it in combination with the Queue structure.


# For example:

# Given binary tree: [3, 9, 20, null, null, 15, 7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:

# [
#   [3],
#   [9,20],
#   [15,7]
# ]\
  
# Breadth First Search Solution
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = []
        queue.append(root)
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                current_node = queue.pop(0)
                current_level.append(current_node.val)  # add node to current level

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)
        return result

# Time Complexity: O(N) where N is the total number of nodes in the tree.

# Space Complexity: O(N), since we need an O(N) space to return the result. We will also need O(N) for the queue.
