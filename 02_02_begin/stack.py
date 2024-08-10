"""
Python Data Structures - A Game-Based Approach
Stack class
"""


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self._stack) == 0

    def __len__(self):
        return len(self._stack)
