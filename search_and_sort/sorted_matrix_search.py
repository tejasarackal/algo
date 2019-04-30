

def naive_search_matrix(matrix, elem):
    col_size = len(matrix[0])
    row_size = len(matrix)
    row, col = 0, col_size - 1

    while row < row_size and col > -1:
        print((row, col), matrix[row][col])
        if matrix[row][col] == elem:
            return row, col
        elif elem > matrix[row][col]:
            row += 1
        else:
            col -= 1


if __name__ == '__main__':
    matrix = []
    for i in range(4):
        matrix.append([t + 2*i for t in range(4)])

    for i in range(4):
        print(matrix[i])

    print(naive_search_matrix(matrix, 6))
