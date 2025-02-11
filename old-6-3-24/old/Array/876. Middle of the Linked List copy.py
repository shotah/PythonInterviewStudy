# The number of nodes in the list is in the range [1, 100].
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        search = head
        node_indexes = []
        index = 0
        while search:
            node_indexes.append(index)
            search = search.next
            index += 1
        middle = int(len(node_indexes) / 2)
        get = head
        index = 0
        while get:
            print(node_indexes[middle])
            if index == node_indexes[middle]:
                return get
            get = get.next
            index += 1
        return None

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
