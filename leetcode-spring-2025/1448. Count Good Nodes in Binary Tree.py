from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, n, s, max_val_so_far):
        if not n:
            return
        if max_val_so_far <= n.val:
            print(f"Good Node: {n.val}, past val: {max_val_so_far}")
            s.append(1)
        else:
            print(f"Bad Node: {n.val}, past val: {max_val_so_far}")
            s.append(0)
        max_val_so_far = max(max_val_so_far, n.val)
        self.dfs(n.left, s, max_val_so_far)
        self.dfs(n.right, s, max_val_so_far)

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_path_of_good = []
        self.dfs(root, node_path_of_good, root.val)
        return sum(node_path_of_good)


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


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case 1: Empty Tree
    input1 = [3, 1, 4, 3, None, 1, 5]
    expected1 = 4
    head1 = create_binary_tree(input1)
    actual1 = Solution().goodNodes(head1)
    assert (
        actual1 == expected1
    ), f"Test Case 1 Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case 1 Passed!")

    # Test Case 1: Empty Tree
    input1 = [3, 3, None, 4, 2]
    expected1 = 3
    head1 = create_binary_tree(input1)
    actual1 = Solution().goodNodes(head1)
    assert (
        actual1 == expected1
    ), f"Test Case 1 Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case 1 Passed!")

    # Test Case 1: Empty Tree
    input1 = [9, None, 3, 6]
    expected1 = 1
    head1 = create_binary_tree(input1)
    actual1 = Solution().goodNodes(head1)
    assert (
        actual1 == expected1
    ), f"Test Case 1 Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case 1 Passed!")

    # Test Case 1: Empty Tree
    input1 = [
        -1,
        5,
        -2,
        4,
        4,
        2,
        -2,
        None,
        None,
        -4,
        None,
        -2,
        3,
        None,
        -2,
        0,
        None,
        -1,
        None,
        -3,
        None,
        -4,
        -3,
        3,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        3,
        -3,
    ]
    expected1 = 5
    head1 = create_binary_tree(input1)
    actual1 = Solution().goodNodes(head1)
    assert (
        actual1 == expected1
    ), f"Test Case 1 Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case 1 Passed!")
