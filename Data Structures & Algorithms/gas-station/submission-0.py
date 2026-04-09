class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #seems like I want to start with the most amount of gas and the list cost, so I have spare gas thru the trip. 
        #Maybe I have to max the differenceof (gas -cost) then test it on a run if it works then return that index if not
        # return -1 
        # this does not work on all cases so failed attempt. 

        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        s_index = 0

        for i in range(len(gas)):
            total_tank += (gas[i] - cost[i])

            if total_tank < 0:
                total_tank = 0
                s_index = i+1
        return s_index