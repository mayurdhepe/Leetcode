class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # non overlapping case
            if start >= prevEnd:
                # update the prevEnd
                prevEnd = end
            else:
                # overlapping, then consider the one with minimum End point
                res += 1
                prevEnd = min(prevEnd, end)
                
        return res
                
        