from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        #initialize a new empty ht to hold set elements 
        self.set = HashTable(elements)

        #track number of elements given 
        self.size = 0 if elements == None else len(self.set)

    def size(self):
        #this method returns the size of the set
        return self.set.size

    def contains(self, element):
        #this method returns a boolean if an element is in the set or not
        return self.set.contains(element)

    