from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == key:
                return node
            stack.extend(filter(None, [node.right, node.left]))
        return root


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

    # Test Case: Delete a node (example)
    input_values = [5, 3, 6, 2, 4, null, 7]
    key_to_delete = 3
    head = create_binary_tree(input_values)  # type: ignore

    # Call the deleteNode function
    updated_head = Solution().deleteNode(head, key_to_delete)

    # Verify that the node with key_to_delete is no longer in the tree
    deleted_node = find_node_with_value(updated_head, key_to_delete)
    assert deleted_node is None, f"Test Case Failed: Node with value {key_to_delete} should be deleted."
    print("Test Case Passed!")
