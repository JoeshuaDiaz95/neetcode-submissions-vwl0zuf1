class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0


        if n == 0:
            return 1
        
        if n < 0 :
            ans = x
            for _ in range(abs(n)+1):
                ans = ans / x

            return ans
        if n > 0: 
            ans = x
            for _ in range(abs(n)-1):
                ans = ans * x
            return ans