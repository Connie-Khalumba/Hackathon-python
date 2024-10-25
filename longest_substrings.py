def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # Set to store unique characters in the current window
    left = 0          # Left pointer for the sliding window
    max_length = 0    # Variable to store the maximum length found

    for right in range(len(s)):
        # If we encounter a repeating character, shrink the window from the left
        while s[index] in char_set:
            char_set.remove(s[left])  # Remove character at left pointer from the set
            left += 1  # Move left pointer to the right
        
        # Add the current character to the set
        char_set.add(s[index])
        
        # Calculate the current window length and update max_length if it's the longest so far
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
input_string = "abcabcbbc"
result = lengthOfLongestSubstring(input_string)
print(f"Length of the longest substring without repeating characters: {result}")
