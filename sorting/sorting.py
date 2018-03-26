#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
       Running time: O(n) checking e/item in the array. 
                     O(1) if first item is not sorted 
                     (return false)
       Memory usage: O(1) with a counter bc it doesn't 
                     count all the ranges
    # Check that all adjacent items are in order, 
    # return early if not"""

    items_len = len(items)

    for index, item in enumerate(items):
        #prevent loop from going out of range
        if index + 1 = items_len: return True #items are sorted
        if item > items[index + 1]: return False #items not sorted
    
    #for items with length == 0
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n) Why and under what conditions?
                  O(n^2) Why and under what conditions?
    Memory usage: O(n^2) Why and under what conditions?"""
    # Repeat until all items are in sorted order
    # Swap adjacent items that are out of order

    items_len = len(items)
    is_sorted = False

    while not (is_sorted):
        #the list is sorted avoiding the swapping of items
        is_sorted = True

        # loop to sort items by swapping adjacent unordered items
        for index, item in enumerate(items):

            #avoid aditional checking once items are sorted
            if index + 1 >= items_len: break

            #items are unordered
            if items_len > items[index + 1]:
                is_sorted = False

                #items are being organized
                items[index], items[index + 1] = items[index + 1], items[index]
        
        #keep last sorted item position to not double check
        items_len -= 1


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Repeat until all items are in sorted order
    # Find minimum item in unsorted items
    # Swap it with first unsorted item

    last_unsorted, is_sorted, smallest_index, items_len = 0, False, 0, range (len(items))
    
    #base condition
    while not is_sorted:

        #generates the swaping of items
        for index in items_len:

            #avoid aditional checking once items are sorted
            if index + 1 == len(items):
                break
            
            #if items are unordered
            if items[smallest_index] > items[index + 1]:
                smallest_index = index + 1

        if last_unsorted == len(items):
            return None

        # the smallest item is swaped with the first unsorted item
        current_sm, unsorted = items[smallest_index], items[last_unsorted]
        items[smallest_index], items[last_unsorted] = unsorted, current_sm

        last_unsorted += 1
        
        # Restart index counter to the first item in the unsorted array
        smallest_index, items_len = last_unsorted, `range(last_unsorted, len(items))
        
        # the loop ends once all items are sorted
        is_sorted = True if last_unsorted == len(items) else False


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Repeat until all items are in sorted order
    # Take first unsorted item
    # Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Repeat until one list is empty
    # Find minimum item in both lists and append it to new list
    # Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    # Split items list into approximately equal halves
    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Choose a pivot any way and document your method in docstring above
    # Loop through all items in range [low...high]
    # Move items less than pivot into front of range [low...p-1]
    # Move items greater than pivot into back of range [p+1...high]
    # Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: ??? Why and under what conditions?
    Worst case running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Check if high and low range bounds have default values (not given)
    # Check if list or range is so small it's already sorted (base case)
    # Partition items in-place around a pivot and get index of pivot
    # Sort each sublist range by recursively calling quick sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    # Create list of counts with a slot for each number in input range
    # Loop over given numbers and increment each number's count
    # Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    # Create list of buckets to store numbers in subranges of input range
    # Loop over given numbers and place each item in appropriate bucket
    # Sort each bucket using any sorting algorithm (recursive or another)
    # Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()