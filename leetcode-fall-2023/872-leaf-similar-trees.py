from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1, s2 = [], []

        def dfs(n, s):
            if not n:
                return
            if not n.left and not n.right:
                s.append(n.val)
                return
            dfs(n.left, s)
            dfs(n.right, s)

        dfs(root1, s1)
        dfs(root2, s2)
        return s1 == s2
