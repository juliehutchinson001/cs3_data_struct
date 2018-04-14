#!python

from linked_list import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return True if self.list.is_empty() else False


    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.size

    #add element to the end of the queue
    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? By appending an item to the
        ll'tail, the time is constant since we have the pointer"""
        # Insert given item
        return self.list.append(item)

    def front(self):
