from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)
#
# Lägger till ett "key-value pair" i trädet. Om nyckeln redan finns så kommer
# värdet kopplat till nyckeln att ersättas med det nya värdet för att se till
# att endast unika nycklar existerar i trädet

    def put(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value, None, None)
            else:
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value, None, None)
            else:
                self.right.put(key, value)
        else:
            self.value = value  # Ersätter värdet

# Returnerar ett str värde för alla nyckelvärden i trädet
    def to_string(self):
        res = ''
        if self.left:
            res += self.left.to_string()
        res += f"{self.key}:{self.value}, "
        if self.right:
            res += self.right.to_string()
        return res  # Returnerar alla str värden

# Returnerar antalet noder i trädet
    def count(self):
        count = 1  # Ser till att startnoden räknas med
        if self.left:
            count += self.left.count()
        if self.right:
            count += self.right.count()
        return count  # Returnerar totala antalet noder

    def get(self, key):
        if self.key == key:  # Om nyckeln matchar den aktuella nodens nyckel
            return self.value

        elif key < self.key and self.left:
            return self.left.get(key)

        elif key > self.key and self.right:  # samma sak för höger
            return self.right.get(key)
        else:
            return None    # annars returnera 0

    def max_depth(self):
        # Beräkna vänstra trädets djup
        left_depth = self.left.max_depth() if self.left else 0

        # Beräkna högra trädets djup
        right_depth = self.right.max_depth() if self.right else 0

        return max(left_depth, right_depth) + 1

    def count_internal_nodes(self):
        count = 0
        if self.left:
            count += 1  # Räkna nod till vänster

            # kalla funktionen rekursivt på vänsterträdet.
            count += self.left.count_internal_nodes()
        if self.right:
            count += 1  # räkna nod till höger

            # kalla funktionen rekursivt på högerträdet.
            count += self.right.count_internal_nodes()

        return count  # returnerar antalet räknade noder

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        if self.left:
            self.left.as_list(lst)

        # Lägg till den aktuella nodens nyckelpar i listan
        lst.append((self.key, self.value))

        if self.right:
            self.right.as_list(lst)

        return lst  # Returnera den sammansatta listan

# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.


@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns an internal node count. That is, the number of nodes
    # that has aleast one child (i.e. not leafs)
    def count_internal_nodes(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal_nodes()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
