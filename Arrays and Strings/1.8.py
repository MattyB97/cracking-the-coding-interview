# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
# Time Complexity: O(NxM)
# Space Complexity: O(NxM)

# Difficult in one pass-through, as the 0s added will then trigger another 0'ing of row/col
# There is possibly a solution that does this in one pass by ignoring all nodes already effected by the 0'ing.
# Quite difficult to implement and would worsen space complexity slightly
def find_zeros(arr: [[]]) -> [[]]:
    zero_indexes = [[]]
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            # print(f'Looking at: [{row}], [{col}], value: {arr[row][col]}')
            if arr[row][col] == 0:
                # print(f'Appending: [{row}], [{col}]')
                zero_indexes.append([row, col])
    del zero_indexes[0]
    return zero_indexes


def zero_matrix(arr: [[]]) -> [[]]:
    """Return an array With All values in the same row or column as a 0 set to 0
    >>> zero_matrix([[1, 2, 3, 4, 5, 6], [0, 1, 1, 1, 1, 1], [2, 1, 2, 0, 0, 0]])
    [[0, 2, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> zero_matrix([[1,2,3],[1,0,5],[2,4,6]])
    [[1, 0, 3], [0, 0, 0], [2, 0, 6]]"""
    zero_indexes = find_zeros(arr)
    for zero_index in zero_indexes:
        # Row Zeroing
        for i in range(len(arr[zero_index[0]])):
            arr[zero_index[0]][i] = 0
        # Col Zeroing
        for j in range(len(arr)):
            arr[j][zero_index[1]] = 0
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
