from dataclasses import dataclass
from typing import List
from math import ceil as c


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_value = 0
        for char in word:
            hash_value = (hash_value * 31) + ord(char)

        return hash_value

    # Doubles size of bucket list
    def rehash(self):
        lst = []
        for bucket in self.buckets:
            lst.extend(bucket)
        numberOfbuckets = self.bucket_list_size() * 2
        self.buckets = [[] for i in range(numberOfbuckets)]
        for word in lst:
            index = self.get_hash(word) % len(self.buckets)
            self.buckets[index].append(word)

    # Adds a word to set if not already added
    def add(self, word):
        index = self.get_hash(word) % len(self.buckets)
        if not self.contains(word):
            self.buckets[index].append(word)
            self.size += 1
            if self.size >= len(self.buckets):
                self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        result = "{ "
        for bucket in self.buckets:
            result += " ".join(bucket) + " "
        result += "}"
        return result

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        index = self.get_hash(word) % len(self.buckets)
        return word in self.buckets[index]

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        index = self.get_hash(word) % len(self.buckets)
        if self.contains(word):
            self.buckets[index].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max_size = max(len(bucket) for bucket in self.buckets)
        return max_size

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        zero_buckets = sum(1 for bucket in self.buckets if len(bucket) == 0)
        return c(zero_buckets / len(self.buckets) * 2) / 2

    # Returns a list with all words in the set
    def as_list(self):
        word_list = []
        for bucket in self.buckets:
            word_list.extend(bucket)
        return word_list
