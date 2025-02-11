from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if list1 and not list2: return list1
        if list2 and not list1: return list2
        merged = None
        if list1 and not list2 or list1 and list2 and list1.val <= list2.val:
            merged = list1
            list1 = list1.next
        elif list2 and not list1 or list1 and list2 and list1.val > list2.val:
            merged = list2
            list2 = list2.next
        result = merged
        while list1 or list2:
            if list1 and not list2 or list1 and list2 and list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
                merged = merged.next
            elif list2 and not list1 or list1 and list2 and list1.val > list2.val:
                merged.next = list2
                list2 = list2.next
                merged = merged.next
        return result

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list1 = ListNode(2)
list2 = ListNode(1)
s = Solution().mergeTwoLists(list1, list2)
print("Solution:")
print(s.val)
while s and s.next:
    s = s.next
    print(s.val)
