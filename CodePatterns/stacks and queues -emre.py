# https://emre.me/data-structures/stacks-and-queues/

# Stacks, like the name suggests, follow Last-In-First-Out (LIFO) principle while Queues work with first come first served approach, in other words with First-In-First-Out (FIFO) principle.

# Implementation of Stacks with Using Lists
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Implementation of Stacks with Using collections.deque class
from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

# Implementation of Queues
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        return self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0
      
# Implementation of Queues with Using collections.deque class
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        return self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0
