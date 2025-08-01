from typing import List

def generate(numRows: int) -> List[List[int]]:
    result = []
    for i in range(numRows):
        temp = []
        for j in range(i+1):
            if i == j or j == 0:
                temp.append(1)
            else:
                temp.append((result[i-1][j-1]+result[i-1][j]))
        result.append(temp)
    return result