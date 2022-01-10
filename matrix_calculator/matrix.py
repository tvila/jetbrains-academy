import copy

def main_menu():
    # Welcome message
    while True:
        print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '4. Transpose matrix', '5. Calculate a determinant', '6. Inverse matrix', '0. Exit', sep="\n")
        usr_choice = int(input('Your choice: '))
        # Logic menu:
        if usr_choice == 1:
            add_matrices()
        elif usr_choice == 2:
            mult_constant()
        elif usr_choice == 3:
            mult_matrices()
        elif usr_choice == 4:
            transpose_matrix()
        elif usr_choice == 5:
            det()
        elif usr_choice == 6:
            inverse_matrix()
        elif usr_choice == 0:
            break
        else:
            print('Error')

def add_matrices():
    # MATRIX A ----------------------------------------------
    size_a = [int(i) for i in input('Enter size of first matrix: ').split()][0]
    print('Enter first matrix:')
    matrix_a = [input().split() for rows in range(size_a)]
    matrix_a = [list(map(float, i)) for i in matrix_a]

    # MATRIX B ----------------------------------------------
    size_b = [int(i) for i in input('Enter size of second matrix: ').split()][0]
    matrix_b = [input().split() for rows in range(size_b)]
    matrix_b = [list(map(float, i)) for i in matrix_b]

    # MATRIX SUM -------------------------------------------
    def matrix_sum(*nested_list):
        matrix_ab = [[sum(items) for items in zip(*zipped_list)] for zipped_list in zip(*nested_list)]
        matrix_ab = [list(map(str, i)) for i in matrix_ab]
        for i in range(len(matrix_ab)):
            print(" ".join(matrix_ab[i]))

    # LOGIC ------------------------------------------------
    if size_a != size_b:
        print('The operation cannot be performed.')
    else:
        print('The result is:')
        matrix_sum(matrix_a, matrix_b)
        print("")


def mult_constant():
    n, m = map(int, input('Enter size of matrix: ').split())
    print('Enter matrix:')
    matrix = [[float(i) for i in input().split()] for rows in range(n)]
    constant = float(input('Enter constant: '))
    matrix_multi = [[str(j * constant) for j in i] for i in matrix]
    print('The result is:')
    for i in matrix_multi:
        print(*i)
    print("")

def mult_matrices():
    # Matrix 1
    n_m1, m_m1 = map(int, input('Enter size of the first matrix: ').split())
    matrix1 = [[float(i) for i in input().split()] for rows in range(n_m1)]

    # Matrix 2
    n_m2, m_m2 = map(int, input('Enter size of the second matrix: ').split())
    matrix2 = [[float(i) for i in input().split()] for rows in range(n_m2)]

    if m_m1 != n_m2:
        print('The operation cannot be performed.')
    else:
        result = [[sum(i * j for i, j in zip(X_row, Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]
        print('The result is:')
        for i in result:
            print(*i)
        print('')

def transpose_matrix():
    def trans_menu():
        print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', sep='\n')
        usr_trans = int(input('Your choice: '))
        if usr_trans == 1:
            main_diagonal()
        elif usr_trans == 2:
            side_diagonal()
        elif usr_trans == 3:
            vertical_line()
        elif usr_trans == 4:
            horizontal_line()
        else:
            print('Error')

    def usr_selection():
        n, m = map(int, input('Enter matrix size: ').split())
        global matrix_trans
        matrix_trans = [[float(i) for i in input().split()] for rows in range(n)]
        print('The result is:')

    def main_diagonal():
        usr_selection()
        main_diagonal = list(map(list, zip(*matrix_trans)))
        for i in main_diagonal:
            print(*i)
        print('')

    def side_diagonal():
        usr_selection()
        side_diagonal = [[matrix_trans[i][j] for i in reversed(range(len(matrix_trans)))] for j in reversed(range(len(matrix_trans[0])))]
        for i in side_diagonal:
            print(*i)
        print('')

    def vertical_line():
        usr_selection()
        vertical = [[matrix_trans[i][j] for j in reversed(range(len(matrix_trans[0])))] for i in range(len(matrix_trans))]
        for i in vertical:
            print(*i)
        print('')

    def horizontal_line():
        usr_selection()
        horizontal = [matrix_trans[i] for i in reversed(range(len(matrix_trans)))]
        for i in horizontal:
            print(*i)
        print('')

    trans_menu()

def det():
    n, m = map(int, input('Enter matrix size: ').split())
    matrix = [[float(i) for i in input().split()] for rows in range(n)]
    print('The result is:')
    print(determinante((matrix)))
    print('')

def determinante(matriz):
    suma = 0
    if len(matriz) == 1 and len(matriz[0]) == 1:
      print(matriz[0][0])

    elif len(matriz) == 2 and len(matriz[0]) == 2:
        suma = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]
        return suma
    else:
        for i in range(len(matriz)):
            aux = copy.deepcopy(matriz)
            aux.remove(matriz[0])
            # print('aux2', aux)
            for j in range(len(aux)):
                aux[j] = aux[j][0:i] + aux[j][i + 1:]

            suma += (-1) ** (i % 2) * matriz[0][i] * determinante(aux)

        return suma


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

def minor_inv(matrix):
    matrix_adj = []
    matrix_Append = []

    if len(matrix) <= 3:

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                minor = getMatrixMinor(matrix, i, j)
                adjunta = (-1) ** (i + j % 2) * (minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0])
                matrix_adj.append(adjunta)

        for i in range(0, len(matrix_adj), len(matrix)):
            matrix_Append.append(matrix_adj[i:i + len(matrix)])

        return matrix_Append
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                adjunta = (-1) ** ((i + j) % 2) * determinante(getMatrixMinor(matrix, i, j))
                matrix_adj.append(adjunta)

        for i in range(0, len(matrix_adj), len(matrix)):
            matrix_Append.append(matrix_adj[i:i + len(matrix)])
        return matrix_Append



def inverse_matrix():
    n, m = map(int, input('Enter matrix size: ').split())
    matrix = [[float(i) for i in input().split()] for rows in range(n)]

    if determinante(matrix) == 0:
        print("This matrix doesn't have an inverse.\n")


    else:
        matrix_trans = list(map(list, zip(*matrix)))
        matriz_adunta = minor_inv(matrix_trans)
        matrix_det = 1 / determinante(matrix)
        matrix_multi = [[round((j * matrix_det), 3) if (j * matrix_det) != 0 else 0 for j in i] for i in matriz_adunta]


        print('The result is:')

        for i in matrix_multi:
            print(*i)
        print('')


