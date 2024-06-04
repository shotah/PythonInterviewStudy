# https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/

# How to identify?
# This approach is quite useful when dealing with reversal of Linked Lists 
# when there is a constraint to do it without using extra memory.

# When the problem gives this constraint and Linked Lists 
# data structure, you should think about In-place Reversal of a Linked List pattern.



# Reverse a singly linked list.

# Example:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

# In-Place Reversal Solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        previous, current, next = None, head, None
        while current is not None:
            next = current.next  # temporarily store the next node
            current.next = previous  # reverse the current node
            previous = current  # point previous to the current node
            current = next  # move on
        return previous
      
# Time Complexity: O(N) where N is the number of nodes in the Linked Lists.
# Space Complexity: O(1), algorithm runs in constant space.
