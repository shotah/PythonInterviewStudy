# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root:
        #     left_val = None
        #     right_val = None
        #     if root.val == val:
        #         return root
        #     if root.left:
        #         left_val = self.searchBST(root.left, val)
        #     if root.right:
        #         right_val = self.searchBST(root.right, val)
        #     return left_val if left_val else right_val
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
