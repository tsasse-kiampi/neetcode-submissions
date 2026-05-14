"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = []
        for s in intervals:
            times.append((s.start, 1))
            times.append((s.end, -1))

        times.sort()

        meet = 0
        for t, delta in times:
            meet += delta
            if meet > 1: return False
            else: continue
        return meet == 0    

               
