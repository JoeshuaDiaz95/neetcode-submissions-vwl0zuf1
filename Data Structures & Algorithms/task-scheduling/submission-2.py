from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)



        maxheap = [(-cnt,task) for task, cnt in freq.items()]

        heapq.heapify(maxheap)
        
        time = 0 

        cooldown = deque()


        while maxheap or cooldown:
            time += 1


            if maxheap:
                cnt,task = heapq.heappop(maxheap)
                cnt += 1

                if cnt < 0:

                    available_time = time + n
                    cooldown.append((available_time, cnt, task))
            if cooldown and cooldown[0][0] == time:
                ready_time, cnt, task = cooldown.popleft()
                heapq.heappush(maxheap,(cnt,task))
        return time




        