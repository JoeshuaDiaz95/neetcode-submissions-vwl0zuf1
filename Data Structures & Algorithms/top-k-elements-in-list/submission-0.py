from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = defaultdict(int)
        answer = []
        currentmaxkey = 0
        for num in nums:
            map1[num]+= 1
        while k > 0:
            currentmaxkey = None
            for key in map1.keys():
                if currentmaxkey is None or map1[key] > map1[currentmaxkey]:
                    currentmaxkey = key
            answer.append(currentmaxkey)
            map1[currentmaxkey] = 0
            k -= 1
        return answer




        