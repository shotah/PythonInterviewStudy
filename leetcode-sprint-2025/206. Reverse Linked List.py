from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


# Helper function to create a linked list from a Python list
def create_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert a linked list to a Python list
def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    output_list = []
    current = head
    while current:
        output_list.append(current.val)
        current = current.next
    return output_list


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case:
    input = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    head = create_linked_list(input)
    actual_head = Solution().reverseList(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")

    # Test Case:
    input = [1, 2]
    expected = [2, 1]
    head = create_linked_list(input)
    actual_head = Solution().reverseList(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")
