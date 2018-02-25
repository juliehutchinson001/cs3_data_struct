#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_recursive(n) 


def factorial_iterative(n):
    # one liner
    # return reduce(lambda x, y: x * y, range(1, n + 1))
    #check for edge case because the factorial of 0 is 1
    if n == 0: return 1
    
    #set counter
    counter = n - 1
    #set result
    final_fact_result = n

    #loop until all of the factorial numbers have been calculated
    while counter > 0:
        #multiply result by the next factorial number
        final_fact_result *= counter
        #set next factorial number
        counter -= 1
    
    return final_fact_result




def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()