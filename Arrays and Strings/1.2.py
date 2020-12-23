# CHECK PERMUTATION: Given two strings, write a method to decide if one is a permutation of the other

def check_permutation_hashmap(string_1: str, string_2: str) -> bool:
    string_1_dict = {}

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def check_permutation_set(string_1: str, string_2: str) -> bool:
    """return True if string_2 is a permutation of string_1; else return false
    >>> check_permutation_set('abc', 'bac')
    True
    >>> check_permutation_set('Taco cat', ' actacoT')
    True
    >>> check_permutation_set('Fred is my name', 'Bill is my name')
    False
    >>> check_permutation_set('', '')
    True
    """
    return set(string_1) == set(string_2)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def check_permutation_dict(string_1: str, string_2: str) -> bool:
    """Returns True if string_2 is a permutation of string_1; else return false
    >>> check_permutation_dict('abc', 'bac')
    True
    >>> check_permutation_dict('Taco cat', ' actacoT')
    True
    >>> check_permutation_dict('Fred is my name', 'Bill is my name')
    False
    >>> check_permutation_dict('', '')
    True
    """
    char_counts = {}
    for char in string_1:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string_2:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] == 0:
            del char_counts[char]
    return len(char_counts) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
