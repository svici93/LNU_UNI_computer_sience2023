from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new_node = Node(n)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nxt = new_node
            self.tail = new_node
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.nxt
        return "{" + ", ".join(result) + "}"

    # Add element n as first entry in deque
    def add_first(self, n):
        new_node = Node(n)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nxt = self.head
            self.head = new_node
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.size == 0:
            print("You can't acces an empty queue.")

        else:
            current = self.head
            while current.nxt:
                current = current.nxt
            return current.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.size == 0:
            print("You can't acces an empty queue.")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("You can't acces an empty queue.")
            return None

        removed_value = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nxt
        self.size -= 1
        return removed_value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):

        if self.size == 0:
            print("You can't acces an empty queue.")
            return None
        if self.size == 1:
            value = self.tail.value
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.nxt != self.tail:
                current = current.nxt
            value = self.tail.value
            self.tail = current
        self.size -= 1
        return value
