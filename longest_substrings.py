class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_length = {}
        i = 0
        count = 0
        char = ""
        while i != len(s) :
            if s[i] not in char:
                char = char + s[i]
                count += 1
                i += 1
                if i == len(s) :
                    substring_length[char] = count
            elif s[i] in char:
                substring_length[char] = count
                char = ""
                count = 0
            
        if len(substring_length) == 0:
            substring_length[s] = len(s)
        return max(substring_length.values())