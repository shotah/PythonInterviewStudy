from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         max_pair_value = 0
#         if not head or not head.next:
#             return max_pair_value
#         curr = head
#         stack = []
#         while curr:
#             stack.append(curr.val)
#             curr = curr.next
#         curr = head
#         size = len(stack)
#         count = 1
#         while count <= size / 2:
#             max_pair_value = max(max_pair_value, curr.val + stack.pop())
#             curr = curr.next
#             count += 1
#         return max_pair_value


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f = head
        s = head
        stack = []
        # Since this is a /2 algo, go to the middle
        while f and f.next:
            f = f.next.next
            stack.append(s.val)
            s = s.next

        ans = 0
        # Now go to the end!
        while s:
            m = stack.pop() + s.val
            ans = max(ans, m)
            s = s.next
        return ans


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
    input = [5, 4, 2, 1]
    expected = 6
    head = create_linked_list(input)
    actual = Solution().pairSum(head)
    assert actual == expected, f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")

    # Test Case:
    input = [4, 2, 2, 3]
    expected = 7
    head = create_linked_list(input)
    actual = Solution().pairSum(head)
    assert actual == expected, f"Test Case Failed: Input: {input}, Expected: {expected}, Actual: {actual}"
    print("Test Case Passed!")
