class Solution:
    def compress(self, chars: list[str]) -> int:
        write_index = 0
        read_index = 0

        while read_index < len(chars):
            char_to_compress = chars[read_index]
            count = 0

            # Count consecutive characters
            while read_index < len(chars) and chars[read_index] == char_to_compress:
                count += 1
                read_index += 1

            # Write the compressed character
            chars[write_index] = char_to_compress
            write_index += 1

            # Write the count if it's greater than 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_index] = digit
                    write_index += 1

        return write_index


if __name__ == "__main__":
    print("Running inline tests:")

    # Test Case 1
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    expected = 6
    actual = Solution().compress(chars)
    assert (
        actual == expected
    ), f"Test Case Failed: Input: {chars}, Expected: {expected}, Actual: {actual}"
    print(chars)
    print("\nInline tests finished.")
