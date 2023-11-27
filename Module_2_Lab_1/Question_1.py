def longest_substring_without_repeating_chars(s):
    """
    Finds the length of the longest substring without repeating characters in a given string.

    Args:
    - s (str): Input string for which the longest substring without repeating characters needs to be found.

    Returns:
    - int: Length of the longest substring without repeating characters.
    """
    char_set = set()  # Set to store encountered characters
    max_length = 0     # Variable to store the length of the longest substring
    start = 0          # Start of the sliding window

    for end in range(len(s)):
        while s[end] in char_set:
            # Remove characters from the start of the window until no repeating characters are found
            char_set.remove(s[start])
            start += 1

        # Add the current character to the set
        char_set.add(s[end])

        # Update the maximum length of the substring
        max_length = max(max_length, end - start + 1)

    return max_length

# Exercise-1
input_str_1 = input()
result_1 = longest_substring_without_repeating_chars(input_str_1)
print(result_1)
                                                                                                                            