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
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    left_pos, right_pos = 0, len(text) - 1
    
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if len(text) < 2:
        return True if is_small_str_palindrome(text, alphabet) else False

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

def is_palindrome_recursive(text, left_pos=None, right_pos=None, found_letter=None):

    if left_pos == None or right_pos == None:
        left_pos, right_pos = 0, len(text) - 1
        found_letter, text = False, text.lower()
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if len(text) < 2:
        return True if is_small_str_palindrome(text, alphabet) else False

    if left_pos > right_pos:
        return True if found_letter else False

    left_char, right_char = text[left_pos], text[right_pos]

    if left_char not in alphabet:
        return is_palindrome_recursive(text, left_pos + 1, right_pos, found_letter)
        
    if right_char not in alphabet:
        return is_palindrome_recursive(text, left_pos, right_pos - 1, found_letter)
        
    if left_char == right_char:
        found_letter = True
        return is_palindrome_recursive(text, left_pos + 1, right_pos - 1, found_letter)
    else:
        return False



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