# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # you have to do a one step and a double step
#         # when the double step hits the end, you know single step is in the middle
#         if head is None or head.next is None:
#             return None
#         one_step = head
#         two_step = copy(head)
#         while two_step.next:
#             if two_step.next.next is not None:
#                 two_step = two_step.next.next
#                 print(f"two val: {two_step.val}") # type: ignore
#             if two_step.next is None or two_step.next.next is None: # type: ignore
#                 print(f"skipping middle node {one_step.next.val}") # type: ignore
#                 print(f"with {one_step.next.next.val}") # type: ignore
#                 one_step = one_step.next.next # type: ignore
#                 return head
#             else:
#                 one_step = one_step.next # type: ignore
#             print(f"one val: {one_step.val}") # type: ignore
#         return head


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head


s = Solution()

list_of_nums = [1, 3, 4, 7, 1, 2, 6]
head = ListNode(list_of_nums.pop(0))
prev = head
for i in list_of_nums:
    newNode = ListNode(i)
    prev.next = newNode
    prev = newNode
og_head = head
while og_head.next:
    print(og_head.val)
    og_head = og_head.next
print("magic:")
newHead = s.deleteMiddle(head)
while newHead.next:
    print(newHead.val)
    newHead = newHead.next
