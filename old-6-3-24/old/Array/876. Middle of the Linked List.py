# The number of nodes in the list is in the range [1, 100].
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

t = [1,2,3,4,5]
t = [1,2,3,4,5,6]
head = ListNode(t.pop(0))
prev = head
for v in t:
    curr = ListNode(v)
    prev.next = curr
    prev = curr

s = Solution().middleNode(head)
if s:
    print(
        s.val
    )
