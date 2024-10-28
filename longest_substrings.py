class Solution:
    @staticmethod
    def length_of_longest_substr(s: str) -> int:
        result = 0
        hash_map = {}
        i = 0
        j = 0
        while j < len(s):
            char = s[j]
            # If a duplicate is found, update i to our stored next valid position
            if char in hash_map:
                i = max(hash_map[char], i)
            result = max(result, j - i + 1)
            # Store the next index for this character, as this will be the next valid position to de-duplicate
            hash_map[char] = j + 1
            j += 1
        return result

# Example usage:
input_string = "abcabcbbc"
result = Solution.length_of_longest_substr(input_string)
print(f"Length of the longest substring without repeating characters: {result}")
