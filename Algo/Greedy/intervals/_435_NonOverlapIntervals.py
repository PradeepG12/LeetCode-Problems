from typing import List

"""Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1"""
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    
    n = len(intervals)
    new_intervals = sorted(intervals, key=lambda x:x[1])
    last_ending_time = new_intervals[0][1]
    selected_intervals = 1
    for i in range(1, n):
        start, end = new_intervals[i]
        if last_ending_time <= start:
            selected_intervals += 1
            last_ending_time = end
    return n - selected_intervals
