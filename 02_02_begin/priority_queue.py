# """
# Python Data Structures - A Game-Based Approach
# Priority Queue Class based on heapq.
# """

"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def put(self, item):
        # Heapq is a min-heap, so we push the item with (priority, index, value)
        # Index is used to avoid comparison issues with equal priority
        heapq.heappush(self._queue, (item[0], self._index, item[1]))
        self._index += 1

    def get(self):
        # Pops the smallest item from the heap
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0
