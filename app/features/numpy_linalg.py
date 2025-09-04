import numpy as np

# Матричное умножение
def matrix_multiplication():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])

    print("\n✅ Матрица A:\n", A)
    print("✅ Матрица B:\n", B)
    print("Элементное умножение:\n", A * B)
    print("Матричное умножение (A @ B):\n", A @ B)  # или np.dot(A, B)


# Транспонирование
def transpose_example():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print("\n✅ Матрица A:\n", A)
    print("A.T:\n", A.T)


# Определитель и ранг
def determinant_and_rank():
    A = np.array([[1, 2],
                  [3, 4]])
    det = np.linalg.det(A)
    rank = np.linalg.matrix_rank(A)

    print("\n✅ Матрица A:\n", A)
    print("Определитель:", det)
    print("Ранг:", rank)


# Обратная матрица
def inverse_matrix():
    A = np.array([[4, 7],
                  [2, 6]])
    inv_A = np.linalg.inv(A)

    print("\n✅ Матрица A:\n", A)
    print("Обратная матрица A^-1:\n", inv_A)
    print("Проверка A @ A^-1:\n", A @ inv_A)  # должно быть ≈ единичной матрицей


# Собственные значения и векторы
def eigen_example():
    A = np.array([[1, 2],
                  [2, 1]])
    vals, vecs = np.linalg.eig(A)

    print("\n✅ Матрица A:\n", A)
    print("Собственные значения:", vals)
    print("Собственные векторы:\n", vecs)


# Решение системы уравнений
def solve_system():
    # 2x + y = 11
    # x - y = 1
    A = np.array([[2, 1],
                  [1, -1]])
    b = np.array([11, 1])

    solution = np.linalg.solve(A, b)
    print("\n✅ Система уравнений Ax = b")
    print("Матрица A:\n", A)
    print("Вектор b:", b)
    print("Решение (x, y):", solution)


# Главная функция урока
def feature_linalg():
    matrix_multiplication()
    transpose_example()
    determinant_and_rank()
    inverse_matrix()
    eigen_example()
    solve_system()

