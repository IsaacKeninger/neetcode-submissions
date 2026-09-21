from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        # We store pairs as (timestamp, value) to easily use binary search
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        values = self.timeMap[key]
        
        # bisect_right finds the insertion point for the timestamp
        # It handles matching or finding the closest element smaller than the target
        idx = bisect.bisect_right(values, (timestamp, chr(127)))
        
        # If idx is 0, it means all stored timestamps are greater than the requested timestamp
        if idx == 0:
            return ""
            
        return values[idx - 1][1]
