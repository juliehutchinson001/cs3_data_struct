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

    def add(self, element):
        #this method adds element to the set if it does not exist
        if self.contains(element): 
            return ValueError("{} element already exists".format(element))
        else:
            self.set.set(element, element)
            self.size += 1

    def remove(self, element):
        #this method removes element from set if exists
        if self.contains(element):
            self.size -= 1
            self.set.delete(element)
        else: 
            return ValueError("element to be removed doesn't exists")

    def ht_keys(self): return self.set.keys()

    def union(self, other_set):
        #return a new set that is the union of this set and other_set
        for element in self.get_keys():
            if other_set.contains(element):
                intersection_set.add_element(element)
        return intersection_set

    def intersection(self, other_set):
        #return a new set that is the intersection of this set and other_set
        for element in self.get_keys():
            if other_set.contains(element):
                intersection_set.add_element(element)
        return intersection_set

    def difference(self, other_set):
        #return a new set that is the difference of this set and other_set
        difference_set = Set(4)
        
        for element in self.get_keys():
            if element not in other_set.get_keys():
                difference_set.add_element(element)
        return difference_set

    def is_subset(self, other_set):
        #return a boolean indicating whether other_set is a subset of this set
        if len(self.get_keys()) > len(other_set.get_keys()):
            return False

        for element in other_set.get_keys():
            if self.contains(element):
                continue
            else:
                return False
        return True

def test_set():
    testing_set = Set()
    testing_set.add("Julie")
    testing_set.add("Hutchinson")
    testing_set.add("welcome")
    testing_set.add("Julie")
    testing_set.contains("Julie")
    testing_set.contains("Hutchinson")
    testing_set.contains("welcome")
    other_set = Set()
    other_set.add("welcome")
    other_set.add("data")
    other_set.add("structures")
    other_set.contains("data")
    other_set.contains("structures")
    other_set.contains("welcome")
    united_set = testing_set.union(other_set)
    print(testing_set.set)
    print(other_set.set)
    print(united_set.set)

if __name__ == '__main__':
    test_set()