# URLify: Replace all spaces in a string with '%20'

def urlify(string: str) -> str:
    """"Return string with all spaces replaced with '%20'
    >>> urlify('Mr John Smith')
    'Mr%20John%20Smith'
    >>> urlify('This is a   silly test')
    'This%20is%20a%20%20%20silly%20test'"""
    return string.replace(' ', '%20')
