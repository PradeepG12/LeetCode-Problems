# from Greedy import findActivitySelection

# data = {
#   "start_time": [2 , 6 , 4 , 10 , 13 , 7],
#   "finish_time": [5 , 10 , 8 , 12 , 14 , 15],
#   "activity": ["Homework" , "Presentation" , "Term paper" , "Volleyball practice" , "Biology lecture" , "Hangout"]
# }
# findActivitySelection(data)
from Greedy import eraseOverlapIntervals
from dp import knapsackBetter

# print(eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))

data = [
    {"W":50, "val":[60, 100, 120], "wt":[10, 20, 30]},
    {"W":8, "val":[10, 40, 50, 70], "wt":[1, 3, 4, 5],},
    {"W":4, "val":[1, 2, 3], "wt":[4, 5, 1]},
    {"W":3, "val":[1, 2, 3], "wt":[4, 5, 6]},
]
run = knapsackBetter

print([run(d["wt"], d["val"], d["W"]) for d in data])