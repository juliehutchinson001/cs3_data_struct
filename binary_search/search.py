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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #sort the array (create a copy of my original array)
    new_array = sorted(array)
    #set a start, middle and end variable to track the org arr and sub arrs
    start = 0
    end = len(new_array) - 1
    middle = (start + end) // 2

    #    new_array = [start, ..., ..., ..., middle, ..., ..., ..., end]
    #                  0              (start + end) // 2        len(n_arr)
    #When the end overlaps the start, the loop breaks (base case)
    while start <= end:
        #item is exactly located at the middle index in the array
        if item == new_array[middle]:
           return middle
    
        #item is in the right half of the original array
        if item > new_array[middle]:
           start = middle + 1

        #item is in the left half of the original array
        elif item < new_array[middle]:
           end = middle - 1

        #update middle index according to location of item in new subarrays
        middle = (start + end) // 2

    #steps:
    # new_array = sort(array)
    # start = 0
    # end = len(new_array) - 1
    # target = item

    # while true:    #(start <= end bc 0 == 0 --index doesn't overlap yet)

    #    new_array = [start, ..., ..., middle, ..., ..., end]

    #    -if new_array[middle] == target:
    #        index = middle
    #        return index
    
    #    -if new_array[middle] > target:
    #        start = 0
    #        end = middle - 1
    
    #    -if new_array[middle] < target:
    #        start = middle + 1
    #        end = len(new_array)
    #        target = item
    
    #    middle = (start + end)/2

def binary_search_recursive(array, item, start=None, end=None):
    if start == None:
        array = sorted(array)
        start = 0
        end = len(array) - 1

    middle = (start + end) // 2
    #    array = [start, ..., ..., middle, ..., ..., end]

    if start > end: return None

    if item == array[middle]: return middle

    if item > array[middle]: start = middle + 1

    elif item < array[middle]: end = middle - 1

    # middle = (start + end) // 2
    return binary_search_recursive(array, item, start, end)
