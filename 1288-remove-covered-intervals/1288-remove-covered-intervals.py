class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        valid_intervals_count = 0
        max_end = -1
        
        for start, end in intervals:
            if end > max_end:
                valid_intervals_count += 1
                max_end = end
                
        return valid_intervals_count