"""
Python Data Structures - A Game-Based Approach
Queue class
"""

from collections import deque


class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self._queue.popleft()
        raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)
