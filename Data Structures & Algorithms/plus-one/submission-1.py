class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        td = 1

        for d in range(len(digits)-1,-1,-1):
                nd = digits[d]
                if td == 1:
                    nd = digits[d] + 1
                    td = 0
                if nd >= 10:
                    td = 1
                    res = [nd - 10] + res
                else:
                    res = [nd] + res
        if td == 1:
            res = [1] + res
        return res

