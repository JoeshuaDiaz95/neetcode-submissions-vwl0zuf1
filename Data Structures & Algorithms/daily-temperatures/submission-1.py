class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        days = [0] * len(temperatures)
        for i in range(len(temperatures)):

            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1

            if j < len(temperatures):
                    days[i] = j - i
        return days
