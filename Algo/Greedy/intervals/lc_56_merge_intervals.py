from typing import List

data = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[4,7],[1,4]]
]

def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    intervals = sorted(intervals, key=lambda x:x[0])
    last_interval = intervals[0]
    result = []
    for i in range(n):
        if last_interval[1] > intervals[i][0]:
            result.append(last_interval)
            last_interval = intervals[i]
        else:
            min_index = min(last_interval[0], intervals[i][0])
            max_index = max(last_interval[1], intervals[i][1])
            last_interval = [min_index, max_index]
    result.append(last_interval)
    return result
print([merge(d) for d in data])