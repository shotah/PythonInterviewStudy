from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      value_arr = []
      first_node = ListNode()
      result_node = first_node
      while l1 or l2:
        value = (
          l1.val + l2.val + value_arr[0]
          if value_arr else
          l1.val + l2.val
        )
        value_arr = list(map(int, str(value)))
        result_node.val = value_arr[-1]
        result_node.next = ListNode()
        result_node = result_node.next
        l1 = l1.next
        l2 = l2.next
      return first_node


# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
while l1:
  print(
    l1.val
  )
  l1 = l1.next

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
while l2:
  print(
    l2.val
  )
  l2 = l2.next


start_node = Solution().addTwoNumbers(l1, l2)
while start_node:
  print(
    start_node.val
  )
  start_node = start_node.next

