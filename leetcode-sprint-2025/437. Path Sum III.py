from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def __init__(self):
#         self.res=0
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         def helper(root,path):
#             if root==None:return
#             path.append(root.val)
#             temp=0
#             for i in range(len(path)-1,-1,-1):
#                 temp+=path[i]
#                 if temp==targetSum:
#                     self.res+=1
#             helper(root.left,path)
#             helper(root.right,path)
#             path.pop(-1)
#         helper(root,[])
#         return self.res


class Solution:
    def __init__(self):
        self.target_sum = None
        self.prefix_sums = {0: 1}
        self.count = 0

    def dfs(self, node, current_path_sum) -> Optional[int]:
        if not node:
            return
        current_path_sum += node.val

        # Check if there's a prefix sum that leads to targetSum ending at current node
        count_of_target_paths = self.prefix_sums.get(
            current_path_sum - self.target_sum, 0
        )
        self.count += count_of_target_paths  # Add to total count

        # Update prefix_sums count for the current_path_sum (for future paths)
        self.prefix_sums[current_path_sum] = (
            self.prefix_sums.get(current_path_sum, 0) + 1
        )

        # Recursively explore left and right subtrees
        self.dfs(node.left, current_path_sum)
        self.dfs(node.right, current_path_sum)

        # Backtrack: Decrement count for current_path_sum as we move up
        self.prefix_sums[current_path_sum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> Optional[int]:
        if not root:
            return 0
        self.target_sum = targetSum
        self.dfs(root, 0)
        return self.count


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
    null = None

    # Test Case:
    input1 = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]
    targetSum = 8
    expected1 = 3
    head1 = create_binary_tree(input1)
    actual1 = Solution().pathSum(head1, targetSum)
    assert (
        actual1 == expected1
    ), f"Test Case Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case Passed!")

    # Test Case:
    input1 = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
    targetSum = 22
    expected1 = 3
    head1 = create_binary_tree(input1)
    actual1 = Solution().pathSum(head1, targetSum)
    assert (
        actual1 == expected1
    ), f"Test Case Failed: Input: {input1}, Expected: {expected1}, Actual: {actual1}"
    print("Test Case Passed!")
