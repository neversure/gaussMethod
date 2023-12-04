myA=[
 [7.0, 2.0, -1.0, 1.0, -1],
 [.0, -6.0, 1.0, 1.0, -2.0],
 [-3.0, 1.0, 8.0, 1.0, 1.0],
 [2.0, 2.0, -3.0, 9.0, .0],
 [1.0, -2.0, -3.0, 1.0, -9.0]
]

myB = [
 39.0,
 7.0,   # m = 13
 2.0,
 15,
 21.0]

def printMatrix(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
             print("\t{1:10.2f}{0}".format(" " if (selected is None
or selected != (row, col)) else "*", A[row][col]), end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))

def swapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def divideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider

def sumRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def Gauss(A, B):
    column = 0
    while (column < len(B)):
        # Ищем максимальный по модулю элемент в i-ом стобце
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row is None:
            print("решений нет")
            return None
        # printMatrix(A, B, (current_row, column))
        if current_row != column:
            # "Переставляем строку с найденным элементом выше
            swapRows(A, B, current_row, column)
            # printMatrix(A, B, (column, column))
        # нормализуем строку с найденным элементом
        divideRow(A, B, column, A[column][column])
        # printMatrix(A, B, (column, column))
        # вычитаем из строк ниже
        for r in range(column + 1, len(A)):
            sumRows(A, B, r, column, -A[r][column])
        # printMatrix(A, B, (column, column))
        column += 1
    # теперь матрица приведена к треугольному виду
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("answer")
    print("\n".join("X{0} =\t{1:10.3f}".format(i + 1, x) for i, x in
enumerate(X)))
    return X


print("intial system")
printMatrix(myA, myB, None)
Gauss(myA, myB)
