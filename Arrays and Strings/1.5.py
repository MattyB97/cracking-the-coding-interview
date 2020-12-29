# One Away: Write a function to check if they are one edit (or zero edits) away from being identical
# Time Complexity: O(n)
# Space Complexity: O(n)
def one_away(s1: str, s2: str) -> bool:
    """Return True if s1 is one character change (diff char, removal of char, insertion of char) away from s2
    >>> one_away('pale', 'ple')
    True
    >>> one_away('pales', 'pale')
    True
    >>> one_away('pale', 'bale')
    True
    >>> one_away('pale', 'bake')
    False"""
    if len(s1) > (len(s2) + 1) or (len(s1) + 1) < len(s2):
        return False
    # If they are the same length, only possible difference is a change in characters,
    # Traverse lists and compare each character
    if len(s1) == len(s2):
        return _replace_check(s1, s2)
    # If they are different length, only True solution is that shorter list has one missing element from longer list
    return _removal_check(s1, s2) if len(s1) > len(s2) else _removal_check(s2, s1)


def _replace_check(s1: str, s2: str) -> bool:
    diff_cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_cnt += 1
            if diff_cnt > 1:
                return False
    return True


def _removal_check(s1: str, s2: str) -> bool:
    diff_cnt = 0
    for i in range(len(s2)):
        if s1[i] != s2[i - diff_cnt]:
            diff_cnt += 1
            if diff_cnt > 1:
                return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
