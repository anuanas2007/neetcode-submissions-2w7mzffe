"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        inte = sorted(intervals, key=lambda x: x.start)
        l = 0

        for i in inte:
            if i.start >= l:
                l = i.end
            else:
                return False
        
        return True

