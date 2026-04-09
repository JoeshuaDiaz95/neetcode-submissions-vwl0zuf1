class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]

        best_l = 0
        best_len = 1  # any single char is a palindrome

        for length in range(1, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True

                    if length > best_len:
                        best_len = length
                        best_l = l

        return s[best_l: best_l + best_len]
