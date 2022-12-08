# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head



nums = [1,2,3,4,5]
n = 2
# nums = [1]
# n = 1
nums = [1,2]
n = 1
nums = [1,2]
n = 0
# [2]
nums = [1,2,3,4,5]
n = 2

head = ListNode(nums.pop(0))
node = head
while len(nums) > 0 :
    node.next = ListNode(nums.pop(0))
    node = node.next


print(f"input: ")
inputs = head
print(inputs.val)
while inputs and inputs.next:
    inputs = inputs.next
    print(inputs.val)


s = Solution().removeNthFromEnd(head, n)


print(f"output: ")
print(s.val)
while s and s.next:
    s = s.next
    print(s.val)
