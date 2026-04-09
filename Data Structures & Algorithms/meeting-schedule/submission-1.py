"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        schedule = defaultdict(int)

        for i in intervals:
            if schedule[i.start] == 0 and schedule[i.end] == 0 :
                for e in range(i.start,i.end):
                    schedule[e] = 1
                
            else:
                return False
        return True


