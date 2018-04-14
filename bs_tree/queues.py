#!python

from linked_list import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""

        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

