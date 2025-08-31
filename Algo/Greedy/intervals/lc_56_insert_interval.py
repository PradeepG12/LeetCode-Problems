from typing import List

datas = [{
    "ip1": [[1,3],[6,9]],
    "ip2": [2,5]
},{
    "ip1": [[1,2],[3,5],[6,7],[8,10],[12,16]],
    "ip2": [4,8]
}]

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    result = []
    has_merged = False
    for i in range(n):
        if intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
        elif intervals[i][0] <= newInterval[1]:
            start = min(intervals[i][0], newInterval[0])
            end = max(intervals[i][1], newInterval[1])
            newInterval = [start, end]
        else:
            if not has_merged:
                result.append(newInterval)
                has_merged = True
            result.append(intervals[i])
    if not has_merged:
        result.append(newInterval)
    return result
