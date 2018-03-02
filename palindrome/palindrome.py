#!python
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    if len(text) < 2: return True

    left_pos, right_pos = 0, len(text) - 1
    
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    found_letter = False 

    while left_pos < right_pos:
        left_char, right_char = text[left_pos], text[right_pos]
        
        if left_char not in alphabet:
            left_pos += 1
            continue

        if right_char not in alphabet:
            right_pos -= 1
            continue

        if left_char == right_char:
            found_letter = True
            left_pos += 1
            right_pos -= 1
        else:
            return False

    return True if found_letter else False

def is_palindrome_recursive(text, start_pos=None, end_pos=None):
    
    if start_pos == None and end_pos == None:
        start_pos = 0
        end_pos = len(text) - 1
        text = text.lower()
        alphabet = 'abbacdefghijklmnopqrstuvwxyz'
        left_char = text[start_pos]
        right_char = text[end_pos]

    while left_char < right_char:
        if len(text) < 2 or text == '':
            return False
        if left_char == right_char:
            is_palindrome_recursive(text, start_pos= start_pos + 1, end_pos=end_pos - 1)
        else:
            return False


    # if start_pos <= end_pos:
        
    return True

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()