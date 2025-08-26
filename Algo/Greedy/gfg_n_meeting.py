data=[
    [[1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]]
]

def maximumMeetings(start,end):
    n = len(start)
    schedule = sorted(list(zip(start, end)), key=lambda x:x[1])
    count = 1
    last_meet = schedule[0]
    for i in range(1, n):
        current_meet = schedule[i]
        if last_meet[1] < current_meet[0]:
            last_meet = current_meet
            count+=1
    return count

d=maximumMeetings(data[0][0], data[0][1])
print(d)