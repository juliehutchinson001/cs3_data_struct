#!python
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def is_small_str_palindrome(text, alphabet):
    '''Checks if a string with the length of 1 or less is a palindrome.
    Returns bool. '''
    # checks following edge cases:
    # text = '' (is a palindrome)
    if len(text) == 0: return True
    else:
        # A single char that is NOT in the alpha (is NOT a palindrome)
        return True if text[0] in alphabet else False

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    #initialize counter to keep track of left char and right char
    left_pos, right_pos = 0, len(text) - 1
    
    #capitals are changed to lower case to test palindrome
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #edge case when palindrome is 'a' or ''
    if len(text) < 2:
        #function to assure palindrome chars are in the alphabet
        return True if is_small_str_palindrome(text, alphabet) else False

    found_letter = False # edge case if text has no alphabet letters

    #base case: if left position is not overlapped by right position
    while left_pos < right_pos:
        #tracker of character left and right within string
        left_char, right_char = text[left_pos], text[right_pos]
        
        #if punctuation present in left char position, then skip it
        if left_char not in alphabet:
            left_pos += 1
            continue

        #if punctuation present in right char position, then skip it
        if right_char not in alphabet:
            right_pos -= 1
            continue
        
        #if characters match
        if left_char == right_char:
            #alphabet char found
            found_letter = True
            #continue to the next character
            left_pos += 1
            right_pos -= 1
        else:
            #not a palindrom
            return False

    #if one of the other conditions match until overlap of chars, and palindrom has alpha chars
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