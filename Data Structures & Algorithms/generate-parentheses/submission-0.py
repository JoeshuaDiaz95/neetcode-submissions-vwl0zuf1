class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, left_amount, right_amount):

            if len(current) == 2 * n:
                result.append(current)
                return
            
            if left_amount < n:
                backtrack(current+"(", left_amount+1, right_amount)
            if right_amount < left_amount:
                backtrack(current+")", left_amount, right_amount+1)
        backtrack("",0,0)
        return result