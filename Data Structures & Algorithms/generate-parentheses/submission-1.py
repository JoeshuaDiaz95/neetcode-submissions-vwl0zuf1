class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current,opencount,closecount):

            if len(current) == 2*n:
                res.append(current)
            
            #adding open
            if opencount < n:
                backtrack(current + "(",opencount+1,closecount)


            #adding close
            if closecount < opencount:
                backtrack(current + ")",opencount,closecount+1)

            
        backtrack("",0,0)

        return res
