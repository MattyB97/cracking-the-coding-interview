# Rotate Matrix: Given an image represented by an NxN matrix, write a method to rotate the image by 90 degrees.
# Extra challenge: Can You do the rotation in place
# Time complexity: O(n*n)
# Space Complexity O(1)


def rotate_matrix(arr: [[]]) -> [[]]:
    rows = len(arr)
    # Since the question constraints the array to NxN, we know col len is consistent
    cols = len(arr[0])
    for row in range(int(rows / 2)):
        temp = 0
        for col in range(row, cols - row - 1):
            temp = arr[row][col]

            # Right to Top
            arr[row][col] = arr[col][rows - row - 1]

            # Bottom to Right
            arr[col][rows - row - 1] = arr[rows - 1 - row][cols - 1 - col]

            # Left to Bottom
            arr[rows - 1 - row][cols - 1 - col] = arr[cols - 1 - col][row]

            # Temp to Left
            arr[cols - 1 - col][row] = temp
    return arr


def display_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
        print('')


if __name__ == "__main__":
    arr = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 5, 2, 4, 3], [5, 1, 4, 2, 3], [3, 2, 4, 1, 5]]
    x = rotate_matrix(arr)
    display_matrix(x)
