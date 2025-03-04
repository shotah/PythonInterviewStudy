from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # null guard clause
        if not head or not head.next:
            return head
        odd = head
        # Get the real even from the back of the odd
        even = head.next
        # stash the head of even while we push even forward
        evenHead = even
        while even and even.next:
            # grab the odd from the even stack
            odd.next = even.next
            # the next odd is now a real odd, move fwd!
            odd = odd.next
            # Grab the even from the odds stack
            even.next = odd.next
            # Next is now even, move forward.
            even = even.next
        # combine the two stacks
        odd.next = evenHead
        # return original head that contains the new sorted stack
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
