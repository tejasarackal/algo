
### Write an algorithm such that if an element in an MxN matrix is 0, its entire row and coumn is set to 0


def setZero(matrix: list):
    rows, cols = set(), set()
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(matrix_len):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for zeroRow in rows:
        matrix[zeroRow] = [0] * matrix_len

    for zeroCol in cols:
        for x in range(matrix_len):
            matrix[x][zeroCol] = 0

    return matrix


if __name__ == '__main__':
    matrix = [[1,2,3], [2,0,0], [3,4,5]]
    print(setZero(matrix))
