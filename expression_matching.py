class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top-down Memorization

            def dfs(i, j):
                  if i >= len(s) and j >= len(p):
                        return True
                  if j >= len(s):
                        return False
                  
                  match = i < len(s) and (s[i] == p[j] or p[j] = ".")
                  if (j + 1) < len(p) and p[j + 1] == "*":
                        dfs(i, j + 2) or #don't use *
                        