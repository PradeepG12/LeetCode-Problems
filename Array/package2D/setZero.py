from typing import List

"""
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

def setZeroMatrix(matrix: List[List[int]]) -> None:
    row_zeros = set()
    col_zeros = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row_zeros.add(i)
                col_zeros.add(j)

    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row_zeros or j in col_zeros:
                matrix[i][j] = 0
    
    print(matrix)

setZeroMatrix([[1,1,1],[1,0,1],[1,1,1]])
setZeroMatrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
setZeroMatrix([[1,0]])