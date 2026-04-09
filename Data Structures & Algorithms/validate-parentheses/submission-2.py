class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(',']':'[','}':'{'}
        stack = []

        for char in s:
            if char in hmap.values():
                stack.append(char)
            elif not stack or stack.pop() != hmap[char]:
                return False
        return not stack
