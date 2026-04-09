class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        res = 0

        sign = -1 if x < 0 else 1

        x = abs(x)

        while x != 0:
            digit = int(x % 10)
            x = int(x/10)

            if res > MAX //10 or res < MIN // 10:
                return 0
            res = res * 10 + digit
        
        res *= sign

        if res < MIN or res > MAX:
            return 0 
        return res