from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        s1counter = Counter(s1)
        window_counter = Counter()

        if len1 > len2:
            return False
        
        for i in range(len(s2)):
            window_counter[s2[i]] += 1

            if i >= len1:
                left_char = s2[i-len1]
                window_counter[left_char] -= 1
                if window_counter[left_char] == 0:
                    del window_counter[left_char]


            if window_counter == s1counter:
                return True
        return False





