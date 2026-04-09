class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = False
        b = False
        c = False


        tempa = triplets[0][0]
        tempb = triplets[0][1]
        tempc = triplets[0][2]

        for r in range(len(triplets)):
            tempa = triplets[r][0]
            tempb = triplets[r][1]
            tempc = triplets[r][2]

            if tempa > target[0] or tempb > target[1] or tempc > target[2]:
                continue
            if tempa == target[0]:
                a = True
            if tempb == target[1]:
                b = True
            if tempc == target[2]:
                c = True 
        return a and b and c   
