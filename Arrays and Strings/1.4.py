# Palindrome Permutation: Given a string, write a function to check if its a permutation of a palindrome.
# Does not need to be limited to just dictionary words


from collections import Counter


def palindrome_check(s: str) -> bool:
    """Return True if a palindrome is possible given the input string s (ignoring spaces and capitalization)
    >>> palindrome_check('Taco Cat')
    True
    >>> palindrome_check('This is most certainly not a palindrome')
    False
    >>> palindrome_check('AaBbCcDdEeFfGgHh Ii     Jj Kk')
    True
    """
    counts = Counter(s.lower().replace(' ', ''))
    odd_count = 0
    for char in counts:
        if counts.get(char) % 2 != 0:
            odd_count += 1
            if odd_count == 2:
                return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
