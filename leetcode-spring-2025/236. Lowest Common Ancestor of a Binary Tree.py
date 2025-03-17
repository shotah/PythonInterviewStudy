from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def __init__(self) -> None:
#         self.ans = None
#         self.p = None
#         self.q = None

#     def dfs(self, node: Optional[TreeNode]) -> bool:
#         if not node:
#             return False
#         left = self.dfs(node.left)
#         right = self.dfs(node.right)
#         mid = node == self.p or node == self.q
#         if mid + left + right >= 2:
#             self.ans = node
#         return mid or left or right

#     def lowestCommonAncestor(
#         self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
#     ) -> Optional[TreeNode]:
#         self.p = p
#         self.q = q
#         self.dfs(root)
#         return self.ans


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


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


def find_node_with_value(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == val:
            return node
        stack.extend(filter(None, [node.right, node.left]))


if __name__ == "__main__":
    print("Running inline tests:")
    null = None

    # Test Case:
    input = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    expected = 3
    head = create_binary_tree(input)
    p_val = 5
    q_val = 1
    p = find_node_with_value(head, p_val)
    q = find_node_with_value(head, q_val)
    actual = Solution().lowestCommonAncestor(head, p, q)
    assert (
        actual.val == expected  # type: ignore
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual.val}"  # type: ignore
    print("Test Case Passed!")

    # Test Case:
    input = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    expected = 5
    head = create_binary_tree(input)
    p_val = 5
    q_val = 4
    p = find_node_with_value(head, p_val)
    q = find_node_with_value(head, q_val)
    actual = Solution().lowestCommonAncestor(head, p, q)
    assert (
        actual.val == expected  # type: ignore
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual.val}"  # type: ignore
    print("Test Case Passed!")
