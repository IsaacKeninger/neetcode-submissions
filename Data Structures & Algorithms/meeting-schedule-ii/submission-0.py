class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0
        
        # 1. Extract and sort starts and ends independently
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        
        start_ptr = 0
        end_ptr = 0
        rooms_needed = 0
        
        # 2. Iterate through all start times
        while start_ptr < len(intervals):
            # If a meeting starts before the earliest ending meeting finishes
            if starts[start_ptr] < ends[end_ptr]:
                rooms_needed += 1  # We need a new room
            else:
                # We can reuse the room; move the end pointer
                end_ptr += 1
            
            # Always move to the next starting meeting
            start_ptr += 1
            
        return rooms_needed
