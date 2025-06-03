# from Greedy import findActivitySelection

# data = {
#   "start_time": [2 , 6 , 4 , 10 , 13 , 7],
#   "finish_time": [5 , 10 , 8 , 12 , 14 , 15],
#   "activity": ["Homework" , "Presentation" , "Term paper" , "Volleyball practice" , "Biology lecture" , "Hangout"]
# }
# findActivitySelection(data)
from Greedy import eraseOverlapIntervals

print(eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))