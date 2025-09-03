import numpy as np
import matplotlib.pyplot as plt

#Создание массивов
def create_arrays():
    arr = np.array([1, 2, 3, 4, 5])
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    arange = np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
    linspace = np.linspace(0, 1, 5)    # равномерно 5 чисел между 0 и 1
    print("\n✅ Базовые массивы:\n", arr, zeros, ones, arange, linspace)
    return arr

#Арифметика и broadcasting
def array_operations():
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])
    print("\n✅ Сложение:", a + b)
    print("✅ Умножение:", a * b)
    print("✅ Broadcasting (a + 5):", a + 5)

#Работа с матрицами
def matrix_operations():
    A = np.random.randint(1, 10, (3, 3))
    B = np.random.randint(1, 10, (3, 3))
    print("\n✅ Матрица A:\n", A)
    print("✅ Матрица B:\n", B)
    print("✅ Сумма:\n", A + B)
    print("✅ Произведение (элементное):\n", A * B)
    print("✅ Матрица A * B (dot):\n", np.dot(A, B))

#Анализ случайной матрицы
def random_matrix_analysis():
    M = np.random.rand(10, 5)   # 10 строк × 5 колонок
    print("\n✅ Матрица M:\n", M)

    print("\nСреднее по колонкам:", M.mean(axis=0))
    print("Максимум по строкам:", M.max(axis=1))
    print("Минимум по строкам:", M.min(axis=1))

    # Нормализация колонок в диапазон [0,1]
    M_norm = (M - M.min(axis=0)) / (M.max(axis=0) - M.min(axis=0))
    print("\n✅ Нормализованная матрица:\n", M_norm)

    # Визуализация heatmap
    plt.imshow(M_norm, cmap="viridis", aspect="auto")
    plt.colorbar(label="Значение")
    plt.title("Heatmap нормализованной матрицы")
    plt.show()


def feature_basis():
    create_arrays()
    array_operations()
    matrix_operations()
    random_matrix_analysis()
