"""
Format of a recursive function:
    - base case: where the function stops
    - cursive case: where the function continues
"""


# Check if a given list of numbers is sorted or not
# TC:O(n) for accessing every element
# SC:O(n) for recursive stack space
def is_sorted(nums):
    if len(nums) == 1:
        return True
    else:
        return nums[0] <= nums[1] and is_sorted(nums[1:])


# Generate all the binary strings of N bits
# Function to product string for appending
def append_to_string(char_to_append, result):
    return [char_to_append + char for char in result]


# Generation function
def binary_strings_with_n_bits(N):
    if N == 0:
        return []
    if N == 1:
        return ["0", "1"]
    else:
        return (append_to_string("0", binary_strings_with_n_bits(N - 1)) +
                (append_to_string("1", binary_strings_with_n_bits(N - 1))))


# Find a path from source (top left) to destination(bottom right) in a matrix
## Finding the 1's leads to the destination
def path_finder(matrix, position):
    col_size = len(matrix)
    row_size = len(matrix[0])

    if position == (row_size - 1, col_size - 1):
        return [(row_size - 1, col_size - 1)]

    x, y = position

    if x + 1 < row_size and matrix[x + 1][y] == 1:
        path = path_finder(matrix, (x + 1, y))
        if path:
            return [(x, y)] + path

    if y + 1 < col_size and matrix[x][y + 1] == 1:
        path = path_finder(matrix, (x, y + 1))
        if path:
            return [(x, y)] + path

    return None


def test_functions():
    nums = [1, 3, 4, 5, 2]
    matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1]]
    binary_strings_with_3_bits = ['000', '001', '010', '011', '100', '101', '110', '111']
    path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]

    assert is_sorted(nums) == False
    print("is_sorted passed")

    assert binary_strings_with_n_bits(3) == binary_strings_with_3_bits
    print("binary_strings_with_n_bits passed")

    assert (path_finder(matrix, (0, 0))) == path
    print("path_finder passed")


if __name__ == '__main__':
    test_functions()
