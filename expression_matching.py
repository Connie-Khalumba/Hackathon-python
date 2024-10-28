def is_match(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (is_match(text, pattern[2:]) or
                (first_match and is_match(text[1:], pattern)))
    else:
        return first_match and is_match(text[1:], pattern[1:])

# Example usage
print(is_match("aab", "c*a*b"))  # Should return True
print(is_match("mississippi", "mis*is*p*."))  # Should return False

### Explanation
#Base Case: If the pattern is empty, the text must also be empty for a match.
#First Match: Check if the first character of the text matches the first character of the pattern or if the pattern starts with ..
#Handling *:
#If the pattern has * as the second character, there are two scenarios:
#Skip the * and the preceding character in the pattern.
#If the first characters match, move to the next character in the text and keep the pattern.
#No *: If there's no *, just move to the next character in both the text and the pattern.
