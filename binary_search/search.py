#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # base case: stop recursion if item was not found
    if len(array) == index:
        return None
    # item has been found
    if array[index] == item:
        return index
    
    #increment index to move towards base case
    index += 1
    return linear_search_recursive(array, item, index)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #steps:
    # array.sort()
    # while true:    #(sub(array) != 0)
    #    start = 0
    #    end = len(array) - 1
    #    index = 
    #    target = item

    #    array = [start, ..., ..., middle, ..., ..., end]

    #    length = end - start #has to be greater or equal than 2
    #    middle = (start + end) // 2

    #    if length < 2:
    #        if start == 0 and array[start] == target: return start
    #        elif array[end] == target: return end
    #        return None

    #    -if array[middle] == target:
    #        index = middle
    #        return index
    #    -if array[middle] > target:
    #        start = 0
    #        end = middle - 1
    #        index = start
    #        target = item
    #        middle = (start + end)/2
    #    -if array[middle] < target:
    #        start = middle + 1
    #        end = len(array)
    #        index = start
    #        target = item
    #        middle = (start + end)/2



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests