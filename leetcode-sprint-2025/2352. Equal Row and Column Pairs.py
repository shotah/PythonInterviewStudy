# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
#         inverted_grid = [
#             [grid[row_i][column_i] for row_i in range(len(grid))]
#             for column_i in range(len(grid[0]) if grid else 0)
#         ]
#         pairs = 0
#         for i, row1 in enumerate(grid):
#             pairs += sum([1 for row2 in inverted_grid if row1 == row2])
#         return pairs


# import collections

# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
#         inverted_grid = [
#             [grid[row_i][column_i] for row_i in range(len(grid))]
#             for column_i in range(len(grid[0]) if grid else 0)
#         ]

#         inverted_grid_row_counts = collections.Counter(tuple(row) for row in inverted_grid) # Count row tuples

#         pairs = 0
#         for i, row1 in enumerate(grid):
#             row_tuple = tuple(row1) # Convert row to tuple for dictionary lookup
#             if row_tuple in inverted_grid_row_counts:
#                 pairs += inverted_grid_row_counts[row_tuple] # Add count from Counter
#         return pairs


from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_count = defaultdict(int)  # Initialize a defaultdict to count row tuples
        count = 0  # Initialize the count of equal pairs

        for row in grid:  # Iterate through each row in the input grid
            row_count[
                tuple(row)
            ] += 1  # Convert row to tuple and increment its count in row_count

        for column in zip(
            *grid
        ):  # Iterate through columns (transposed grid) using zip(*grid)
            count += row_count[
                column
            ]  # Convert column to tuple and add its count from row_count to the total

        return count


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    expected = 1
    actual = Solution().equalPairs(grid)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {grid}, Expected: {expected}, Actual: {actual}"

    # Test Case
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    expected = 3
    actual = Solution().equalPairs(grid)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {grid}, Expected: {expected}, Actual: {actual}"

    # Test Case
    grid = [[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
    expected = 3
    actual = Solution().equalPairs(grid)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {grid}, Expected: {expected}, Actual: {actual}"
