from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
      count = 0
      if root is None: return count
      if root.left:
        count += self.countNodes(root.left)
      if root.right:
        count += self.countNodes(root.right)
      count += 1
      return count


# [1,2,3,4,5,6]
l1 = TreeNode(1)
l1.left = TreeNode(2)
l1.right = TreeNode(3)
l1.left.left = TreeNode(4)
l1.left.right = TreeNode(5)
l1.left.right.left = TreeNode(6)
l1.right.right = TreeNode(7)
print(l1.left.left.val)

count = Solution().countNodes(root=l1)
print(count)

# while start_node:
#   print(
#     start_node.val
#   )
#   start_node = start_node.right

