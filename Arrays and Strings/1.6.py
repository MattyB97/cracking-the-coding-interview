# String Compression: Compress a string using the counts of repeated characters.
# If the compressed string is longer than the original, return the original
# Ex. aabcccccaaa -> a2b1c5a3
# Ex. AaBb -> AaBb since A1a1B1b1 is longer
# Time Complexity: O(n)
# Space Complexity: O(n)
def string_compressor(string: str) -> str:
    """Returns a compressed version of the string input unless the compressed version is longer than the original
    >>> string_compressor('aabcccccaaa')
    'a2b1c5a3'
    >>> string_compressor('abcdefg')
    'abcdefg'
    >>> string_compressor('AaaBBCCCCcccc')
    'A1a2B2C4c4'"""
    compressed_string = ''
    i = 0
    while i < len(string):
        char = string[i]
        char_count = 0
        compressed_string = compressed_string + char
        while i < len(string) and string[i] == char:
            char_count += 1
            i += 1
        compressed_string = compressed_string + str(char_count)
    return compressed_string if len(compressed_string) < len(string) else string


if __name__ == "__main__":
    import doctest

    doctest.testmod()