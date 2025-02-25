from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#         result = first_tracker = second_tracker = ListNode(0, head)
#         while second_tracker.next and second_tracker.next.next:
#             first_tracker = first_tracker.next
#             second_tracker = second_tracker.next.next
#         first_tracker.next = first_tracker.next.next
#         return result.next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast = slow = head
        dummy = ListNode(-1, head)
        prev = dummy
        while fast and fast.next:
            fast = fast.next.next
            prev = prev.next
            slow = slow.next
        prev.next = slow.next
        return dummy.next


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

    # Test Case 1: Empty list
    head = create_linked_list([])
    expected = []
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 1 Failed: Input: [], Expected: {expected}, Actual: {actual}"
    print("Test Case 1 Passed!")

    # Test Case 2: Single node list
    head = create_linked_list([1])
    expected = []
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 2 Failed: Input: [1], Expected: {expected}, Actual: {actual}"
    print("Test Case 2 Passed!")

    # Test Case 3: Two node list
    head = create_linked_list([1, 2])
    expected = [1]
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 3 Failed: Input: [1, 2], Expected: {expected}, Actual: {actual}"
    print("Test Case 3 Passed!")

    # Test Case 4: Three node list (odd length)
    head = create_linked_list([1, 2, 3])
    expected = [1, 3]
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 4 Failed: Input: [1, 2, 3], Expected: {expected}, Actual: {actual}"
    print("Test Case 4 Passed!")

    # Test Case 5: Four node list (even length)
    head = create_linked_list([1, 2, 3, 4])
    expected = [1, 2, 4]
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 5 Failed: Input: [1, 2, 3, 4], Expected: {expected}, Actual: {actual}"
    print("Test Case 5 Passed!")

    # Test Case 6: Five node list (odd length)
    head = create_linked_list([1, 2, 3, 4, 5])
    expected = [1, 2, 4, 5]
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 6 Failed: Input: [1, 2, 3, 4, 5], Expected: {expected}, Actual: {actual}"
    print("Test Case 6 Passed!")

    # Test Case 7: Six node list (even length)
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    expected = [1, 2, 3, 5, 6]
    actual_head = Solution().deleteMiddle(head)
    actual = linked_list_to_list(actual_head)
    assert (
        actual == expected
    ), f"Test Case 7 Failed: Input: [1, 2, 3, 4, 5, 6], Expected: {expected}, Actual: {actual}"
    print("Test Case 7 Passed!")

    print("All inline tests passed!")
