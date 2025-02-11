# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:      
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return -1
        result = 0
        queue = []
        queue.append(root)
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                current_node = queue.pop(0)
                if low <= current_node.val <= high:
                    result += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return result

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
low = 7
high = 15
s = Solution().rangeSumBST(root, low, high)
print(s)
