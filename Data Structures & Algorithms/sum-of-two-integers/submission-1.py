class Solution:
    def getSum(self, a: int, b: int) -> int:


        MASK = 0xFFFFFFFF       # 32 bits of 1s
        MAX_INT = 0x7FFFFFFF    # largest positive 32-bit int

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # convert back from 32-bit signed
        return a if a <= MAX_INT else ~(a ^ MASK)
        