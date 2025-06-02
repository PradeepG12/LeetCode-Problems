"""
data = {
  "start_time": [2 , 6 , 4 , 10 , 13 , 7],
  "finish_time": [5 , 10 , 8 , 12 , 14 , 15],
  "activity": ["Homework" , "Presentation" , "Term paper" , "Volleyball practice" , "Biology lecture" , "Hangout"]
}
"""
def findActivitySelection(data):

    # Combine the data into a list of tuples and sort by finish_time (2nd value)
    activities = list(zip(data["start_time"], data["finish_time"], data["activity"]))
    activities.sort(key=lambda x: x[1])
    n = len(activities)
    print(activities) 
    op = [activities[0]]
    last_finish_time = activities[0][1]

    for i in range(1, n):
        start, end, _ = activities[i]
        if last_finish_time <= start:
            op.append(activities[i])
            last_finish_time = end
        
    print(op)
