'''
 01 02 03 04
 05 06 07 08
 09 10 11 12
 13 14 15 16

 13 09 05 01
 14 10 06 02
 15 11 07 03
 16 12 08 04

  row[x] = col[n - x]
  
  00 - 30
  30 - 33
  33 - 03
  03 - 00

'''


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(0,int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top

    return matrix


if __name__ == '__main__':
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    print(matrix)
    matrix2 = rotate_matrix(matrix)
    print(matrix2)