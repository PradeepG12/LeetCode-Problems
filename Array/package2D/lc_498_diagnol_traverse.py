from typing import List

datas = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
    [[1,2],[3,4]]
]

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    m = len(mat)
    n = len(mat[0])
    i = 0
    j = 0
    result = []
    direction = 1
    while i < m and j < n:
        result.append(mat[i][j])

        if direction == 1: 
            if j == n - 1:  
                i += 1
                direction = -1
            elif i == 0:    
                j += 1
                direction = -1
            else:           
                i -= 1
                j += 1
        else:
            if i == m - 1:  
                j += 1
                direction = 1
            elif j == 0:    
                i += 1
                direction = 1
            else:           
                i += 1
                j -= 1

    print(result)
findDiagonalOrder(datas[0])