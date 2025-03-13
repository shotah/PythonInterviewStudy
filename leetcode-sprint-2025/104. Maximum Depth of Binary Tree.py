from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
#         return 1 + max(left_depth, right_depth)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


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
            output_list.append(None)  # Represent null nodes in level order
    # Remove trailing None values for cleaner output if needed
    while output_list and output_list[-1] is None:
        output_list.pop()
    return output_list


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case 1: Empty Tree
    input1 = []
    expected1 = 0
    head1 = create_binary_tree(input1)
    actual1 = Solution().maxDepth(head1)
    assert (
        actual1 == expected1
    ), f"Test Case 1 Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case 1 Passed!")

    # Test Case 2: Single Node Tree
    input2 = [1]
    expected2 = 1
    head2 = create_binary_tree(input2)
    actual2 = Solution().maxDepth(head2)
    assert (
        actual2 == expected2
    ), f"Test Case 2 Failed: Input: {input2}, Expected: {expected2}, Actual: {actual2}"
    print("Test Case 2 Passed!")

    # Test Case 3: Simple Tree Depth 2 (balanced)
    input3 = [3, 9, 20, None, None, 15, 7]
    expected3 = 3
    head3 = create_binary_tree(input3)
    actual3 = Solution().maxDepth(head3)
    assert (
        actual3 == expected3
    ), f"Test Case 3 Failed: Input: {input3}, Expected: {expected3}, Actual: {actual3}"
    print("Test Case 3 Passed!")

    # Test Case 4: Unbalanced Tree (left-heavy)
    input4 = [1, 2, None, 3, None, 4, None, 5]
    expected4 = 5
    head4 = create_binary_tree(input4)
    actual4 = Solution().maxDepth(head4)
    assert (
        actual4 == expected4
    ), f"Test Case 4 Failed: Input: {input4}, Expected: {expected4}, Actual: {actual4}"
    print("Test Case 4 Passed!")

    # Test Case 5: Skewed Tree (right-heavy)
    input5 = [1, None, 2, None, 3, None, 4, None, 5]
    expected5 = 5
    head5 = create_binary_tree(input5)
    actual5 = Solution().maxDepth(head5)
    assert (
        actual5 == expected5
    ), f"Test Case 5 Failed: Input: {input5}, Expected: {expected5}, Actual: {actual5}"
    print("Test Case 5 Passed!")

    print("All inline tests passed!")
