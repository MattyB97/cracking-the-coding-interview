# IS UNIQUE: Implement an algorithm to determine if a string has all unique
# characters. What if you cannot use additional data structures?


# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)
def check_unique_list(string: str) -> bool:
    """Return boolean if it is a unique string or not
    >>> check_unique_list('abcdefgABC')
    True
    >>> check_unique_list('aaa')
    False
    """

    unique_chars = []
    for char in string:
        if char in unique_chars:
            return False
        unique_chars.append(char)
    return True


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def check_unique_set(string: str) -> bool:
    """Return boolean if it is a unique string or not
    >>> check_unique_set('abcdefgABC')
    True
    >>> check_unique_set('aaa')
    False
    """
    return len(set(string)) == len(string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
