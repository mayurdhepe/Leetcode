class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort on basis of start
        intervals.sort(key = lambda i : i[0])
        # add first interval in output
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                # overlapping case
                # [1, 5], [2, 4]
                output[-1][1] = max(lastEnd, end)
            else:
                # non-overlapping
                # [1, 5], [7, 8]
                output.append([start, end])
                
        return output