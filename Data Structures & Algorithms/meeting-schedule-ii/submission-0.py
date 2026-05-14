"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        times = []
        for s in intervals:
            times.append((s.start, 1))
            times.append((s.end, -1))

        times.sort() 

        current = 0
        max_meet = 0

        for _, delta in times:
            current += delta
            max_meet = max(max_meet, current)

        return max_meet       
        