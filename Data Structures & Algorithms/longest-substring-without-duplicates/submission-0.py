class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        start = 0
        seen = {}

        for end in range(len(s)):
            char = s[end]
            
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            
            seen[char] = end
            max_l = max (max_l, end -start +1)
        return max_l