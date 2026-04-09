class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lsmap = {}
        size = 0
        end = 0
        result = []
        for i in range(len(s)):
            lsmap[s[i]] = i
        
        for i in range(len(s)):
            if lsmap[s[i]] > end:
                end = lsmap[s[i]]
            size += 1
            if i == end:
                result.append(size)
                size = 0
                continue
        return result
            
        
        