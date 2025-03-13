from typing import List, Optional, Union


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


# Helper function to create a binary tree from a list (level order) - assuming it's already defined
def create_binary_tree(values: List[Union[int, None]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current_node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            left_node = TreeNode(values[i])  # type: ignore
            current_node.left = left_node
            queue.append(left_node)
        i += 1
        if i < len(values) and values[i] is not None:
            right_node = TreeNode(values[i])  # type: ignore
            current_node.right = right_node
            queue.append(right_node)
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
            output_list.append(None)  # Represent null nodes in level order
    # Remove trailing None values for cleaner output if needed
    while output_list and output_list[-1] is None:
        output_list.pop()
    return output_list


if __name__ == "__main__":
    print("Running inline tests for leafSimilar:")

    # Test Case 5: Example 1 from problem description - Leaf Similar
    root1_values = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2_values = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    expected = True
    root1 = create_binary_tree(root1_values)
    root2 = create_binary_tree(root2_values)
    actual = Solution().leafSimilar(root1, root2)
    assert (
        actual == expected
    ), f"Test Case 5 Failed: Input1: {root1_values}, Input2: {root2_values}, Expected: {expected}, Actual: {actual}"
    print("Test Case 5 Passed!")

    # Test Case 6: Example 2 from problem description - Not Leaf Similar
    root1_values = [1, 2, 3]
    root2_values = [1, 3, 2]
    expected = False
    root1 = create_binary_tree(root1_values)  # type: ignore
    root2 = create_binary_tree(root2_values)  # type: ignore
    actual = Solution().leafSimilar(root1, root2)
    assert (
        actual == expected
    ), f"Test Case 6 Failed: Input1: {root1_values}, Input2: {root2_values}, Expected: {expected}, Actual: {actual}"
    print("Test Case 6 Passed!")

    # Test Case 7: Trees with different structure but same leaf sequence - Leaf Similar
    root1_values = [1, 2]
    root2_values = [1, None, 2]
    expected = True
    root1 = create_binary_tree(root1_values)
    root2 = create_binary_tree(root2_values)
    actual = Solution().leafSimilar(root1, root2)
    assert (
        actual == expected
    ), f"Test Case 7 Failed: Input1: {root1_values}, Input2: {root2_values}, Expected: {expected}, Actual: {actual}"
    print("Test Case 7 Passed!")

    # Test Case 8: More complex trees with same leaf sequence - Leaf Similar
    root1_values = [1, 2, 3, 4, 5, None, 6, None, None, 7, None, None, 8]
    root2_values = [1, 2, 3, None, 5, 4, 6, None, None, 7, 8]
    expected = True
    root1 = create_binary_tree(root1_values)
    root2 = create_binary_tree(root2_values)
    actual = Solution().leafSimilar(root1, root2)
    assert (
        actual == expected
    ), f"Test Case 8 Failed: Input1: {root1_values}, Input2: {root2_values}, Expected: {expected}, Actual: {actual}"
    print("Test Case 8 Passed!")

    # Test Case 9: Trees with different leaf sequences - Not Leaf Similar
    root1_values = [1, 2, 3, 4]
    root2_values = [1, 2, 3, 5]
    expected = False
    root1 = create_binary_tree(root1_values)
    root2 = create_binary_tree(root2_values)
    actual = Solution().leafSimilar(root1, root2)
    assert (
        actual == expected
    ), f"Test Case 9 Failed: Input1: {root1_values}, Input2: {root2_values}, Expected: {expected}, Actual: {actual}"
    print("Test Case 9 Passed!")

    print("All inline tests for leafSimilar passed!")
