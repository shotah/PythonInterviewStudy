from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      value_arr = []
      carry_over = 0
      result_node = first_node = ListNode()
      while l1 or l2 or (carry_over > 0):
        value = carry_over
        if l1:
          value += l1.val
          l1 = l1.next
        if l2:
          value += l2.val
          l2 = l2.next
        value_arr = list(map(int, str(value)))
        if len(value_arr) >= 2:
          print("value_arr",value_arr)
          carry_over = value_arr[0]
          result_node.val = value_arr[-1]
        else:
          print("value",value)
          carry_over = 0
          result_node.val = value
        if l1 or l2 or (carry_over > 0):
          result_node.next = ListNode()
          result_node = result_node.next
      return first_node


# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

start_node = Solution().addTwoNumbers(l1, l2)
while start_node:
  print(
    start_node.val
  )
  start_node = start_node.next

