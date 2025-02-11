# https://emre.me/coding-patterns/fast-slow-pointers/

# How to identify?
# This approach is quite useful when dealing with cyclic Linked Lists or Arrays.

# When the problem involves something related to cyclic 
# data structures, you should think about Fast & Slow Pointers pattern.


# Example 1:

# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to 
# the second node.

# Example 2:

# Input: head = [1, 2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to 
# the first node.

# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Fast & Slow Pointers Solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True  # found the cycle
        return False
      
# inked List Cycle II
# Example 1:

# Input: head = [3, 2, 0, -4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to 
# the second node.
# Circular Linked List - Test 1

# Example 2:

# Input: head = [1, 2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to 
# the first node.
# Circular Linked List - Test 2

# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Fast & Slow Pointers Solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                current = head
                while current is not slow:
                    current = current.next
                    slow = slow.next
                return slow
        return None
