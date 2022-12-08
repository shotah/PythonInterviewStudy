# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 1 and not head.next:
            return None
        sptr = head
        count = 0
        while count <= n:
            if count == n-1 and sptr.next and not sptr.next.next:
                sptr.next = None
            if count == n and sptr and sptr.next:
                sptr.next = sptr.next.next  
            if sptr and sptr.next:
                sptr = sptr.next
            count += 1
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
