from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for letter in s:
            map1[letter]+= 1
        for lettert in t:
            map2[lettert]+= 1
        
        if map1 == map2:
            return True
        else: 
            return False