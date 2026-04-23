class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set()
        res = 0

        for num in nums:
            numset.add(num)
        

        for n in nums: 

            if (n-1) not in numset:
                tmpres = 1
                tmpn = n
                while (tmpn+1) in numset:
                    tmpres += 1
                    tmpn += 1
                
                res = max(res, tmpres)
        return res