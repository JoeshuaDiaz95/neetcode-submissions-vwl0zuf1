class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        currn = n
        
        while currn not in visited:
            visited.add(currn)
            
            # 1. Reset the sum for the digits of the current number
            next_sum = 0
            for char in str(currn):
                digit = int(char)
                next_sum += digit * digit
            
            # 2. Update currn to be the NEW sum
            currn = next_sum
            
            if currn == 1:
                return True # Capital T for Python!
                
        return False