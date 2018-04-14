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
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        return self.list.head.data if not self.list.is_empty() else None

    #remove the oldest element from the front of the queue
    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? changing the ll head pointer is
        constant time"""
        # Remove and return front item, if any
        if self.list.is_empty() == True:
            raise ValueError('queue is empty: {}'.format(self))
        #save top item in the queue
        top_item = self.list.head.data
        #deleting top item from queue
        self.list.delete(top_item)

        # Remove and return top item, if any
        return top_item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(n) – Why? shifting positions within an arr
        represents shuffling through each of the items"""
        # Insert given item
        return self.list.insert(0, item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        return self.list[-1] if not self.is_empty() else None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? the last item can be easily 
        accessed through the index, so it represents constant time"""
        # Remove and return front item, if any
        # Remove and return front item, if any
        
        return self.list.pop() if not self.is_empty() else None


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue