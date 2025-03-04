from typing import Optional, List, Self, Union
from enum import Enum


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self, val=0, left: Optional[Self] = None, right: Optional[Self] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.path_length = 0

    def dfs(self, node: Optional[TreeNode], wasRight: bool, steps: int):
        if not node:
            return None
        # set largest path so far:
        self.path_length = max(self.path_length, steps)

        # if last one was Right:
        if wasRight:
            # Old path continues
            self.dfs(node.left, False, steps + 1)
            # New path gets reset
            self.dfs(node.right, True, 1)
        else:
            # New path gets reset
            self.dfs(node.left, False, 1)
            # Old path continues
            self.dfs(node.right, True, steps + 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root, True, 0)
        return self.path_length


# Helper function to create a binary tree from a list (level order)
def create_binary_tree(values: List[Union[int, None]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current_node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current_node.left = TreeNode(values[i])  # type: ignore
            queue.append(current_node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])  # type: ignore
            queue.append(current_node.right)
        i += 1
    return root


# Helper function (not needed for maxDepth tests, but could be useful for other tree problems)
def tree_to_list_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    output_list: List[Optional[int]] = []
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        if current_node:
            output_list.append(current_node.val)
            queue.append(current_node.left)  # type: ignore
            queue.append(current_node.right)  # type: ignore
        else:
            output_list.append(None)  # Represent None nodes in level order
    # Remove trailing None values for cleaner output if needed
    while output_list and output_list[-1] is None:
        output_list.pop()
    return output_list


def print_tree_indented(node, indent=""):
    if node is None:
        print(indent + "null")
        return
    print(indent + str(node.val))
    print_tree_indented(node.left, indent + "  ")
    print_tree_indented(node.right, indent + "  ")


if __name__ == "__main__":
    print("Running inline tests:")
    null = None

    # Test Case:
    input = [1, null, 1, 1, 1, null, null, 1, 1, null, 1, null, null, null, 1]
    expected = 3
    head = create_binary_tree(input)
    actual = Solution().longestZigZag(head)
    assert (
        actual == expected
    ), f"Test Case Failed: input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")

    # Test Case:
    input = [1, 1, 1, null, 1, null, null, 1, 1, null, 1]
    expected = 4
    head = create_binary_tree(input)
    actual = Solution().longestZigZag(head)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")
