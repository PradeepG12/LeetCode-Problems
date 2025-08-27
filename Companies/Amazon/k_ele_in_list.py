from collections import Counter, defaultdict

items = [1, 2, 5, 4, 5]
m = 3
startIndex = [0, 0, 1]
endIndex   = [1, 2, 2]
query = [2, 4]

def findQueryList(items, m, start, end, query):
    new_list = defaultdict(int)
    for i in range(m):
        for j in range(start[i], end[i]+1):
            new_list[items[j]] += 1
    output = []
    for q in query:
        answer=0
        for key, val in new_list.items():
            if key < q:
                answer += val
        output.append(answer)
    return output

d = findQueryList(items, m, startIndex, endIndex, query)
print(d)