from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        #initialize a new empty ht to hold set elements 
        self.set = HashTable(elements)

        #track number of elements given 
        self.size = 0 if elements == None else len(self.set)

    