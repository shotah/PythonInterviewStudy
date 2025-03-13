from collections import deque
from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        right_edge = []
        prev_node = root
        while queue:
            level_node_qty = len(queue)
            for _ in range(level_node_qty):
                # work inside of level
                node = queue.popleft()
                prev_node = node
                # Extend stack to do whatever you want.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if prev_node:
                right_edge.append(prev_node.val)
        return right_edge


def find_node_with_value(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == val:
            return node
        stack.extend(filter(None, [node.right, node.left]))


# Helper function to create a binary tree from a list (level order)
def create_binary_tree(values: list[Union[int, None]]) -> Optional[TreeNode]:
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


if __name__ == "__main__":
    print("Running inline tests:")
    null = None

    # Test Case: Simple right side view
    input = [1, 2, 3, null, 5, null, 4]
    expected = [1, 3, 4]
    head = create_binary_tree(input)
    actual = Solution().rightSideView(head)
    assert actual == expected, f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")

    # Test Case 2: Another right side view example
    input2 = [1, 2, 3, 4, null, null, null, 5]
    expected2 = [1, 3, 4, 5]
    head2 = create_binary_tree(input2)
    actual2 = Solution().rightSideView(head2)
    assert (
        actual2 == expected2
    ), f"Test Case 2 Failed: Input: {input2}, Expected: {expected2}, Actual: {actual2}"
    print("Test Case 2 Passed!")

    # Test Case: Simple right side view
    input = [1, null, 3]
    expected = [1, 3]
    head = create_binary_tree(input)
    actual = Solution().rightSideView(head)
    assert actual == expected, f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")
