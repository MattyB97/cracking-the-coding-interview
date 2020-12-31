# String Rotation: Check if string s2 is a rotation of s1
# Time Complexity: O(n) where n = s1
# Space Complexity: O(n) where n = s1

def is_substring(s1: str, s2: str) -> str:
    """Returns True if s2 is a rotation of s1
>>> is_substring('waterbottle', 'erbottlewat')
True
>>> is_substring('hello', 'world')
False"""
    if len(s1) != len(s2):
        return False
    s1 += s1
    return s2 in s1

