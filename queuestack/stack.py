#!python

from linked_list import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return True if self.list.is_empty() else False

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? Inserting at the top of the ll (only one
        iteration bc head is on top)"""
        # Push given item
        return self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        return self.list.head.data if self.list.is_empty() == False else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? Removing the item at the top of the
        stack (meaning only one search)"""
        if self.is_empty() == True:
            raise ValueError('stack is empty: {}'.format(self))
        #save top item in the stack
        top_item = self.list.head.data
        #deleting top item from stack
        self.list.delete(self.list.head.data)

        # Remove and return top item, if any
        return top_item



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return True if len(self.list) == 0 else False

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? only one insertion to the
        top of stack as long as there is space (avoid stack
        overflow)"""
        # Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        return self.list[-1] if !(self.is_empty()) else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # Remove and return top item, if any


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack