from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


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
    expected = [1, 3, 5, 2, 4]
    head = create_linked_list(input)
    actual_head = Solution().oddEvenList(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")

    # Test Case:
    input = [2, 1, 3, 5, 6, 4, 7]
    expected = [2, 3, 6, 7, 1, 5, 4]
    head = create_linked_list(input)
    actual_head = Solution().oddEvenList(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")
