# app/features/numpy_indexing.py

import numpy as np

# Индексация и срезы 1D массива
def indexing_1d():
    arr = np.arange(10)   # [0 1 2 3 4 5 6 7 8 9]
    print("\n✅ Исходный массив:", arr)

    print("Первый элемент:", arr[0])
    print("Последний элемент:", arr[-1])
    print("Срез с 2 по 5:", arr[2:6])
    print("Первые 5 элементов:", arr[:5])
    print("Каждый второй элемент:", arr[::2])


# Срезы и индексация в 2D матрицах
def indexing_2d():
    M = np.arange(1, 13).reshape(3, 4)  # 3 строки × 4 колонки
    print("\n✅ Матрица M:\n", M)

    print("Элемент (0,0):", M[0, 0])
    print("Элемент (1,2):", M[1, 2])
    print("Первая строка:", M[0, :])
    print("Вторая колонка:", M[:, 1])
    print("Подматрица (строки 1:, колонки 2:):\n", M[1:, 2:])


# Булевы маски (фильтрация)
def boolean_masks():
    arr = np.array([3, 7, 2, 9, 1, 6])
    mask = arr > 5
    print("\n✅ Исходный массив:", arr)
    print("Булева маска (arr > 5):", mask)
    print("Фильтрация (arr[arr > 5]):", arr[mask])
    print("Только чётные:", arr[arr % 2 == 0])


# Практика: фильтрация датасета
def dataset_filtering():
    temps = np.array([12, 18, 25, 30, 22, 15, 10])
    hot_days = temps[temps > 20]
    print("\n✅ Температуры:", temps)
    print("Жаркие дни (>20°):", hot_days)


# Продвинутое индексирование
def advanced_indexing():
    arr = np.array([10, 20, 30, 40, 50])
    print("\n✅ Исходный массив:", arr)
    print("Выбор элементов [0,2,4]:", arr[[0, 2, 4]])

    M = np.arange(1, 10).reshape(3, 3)
    print("\n✅ Матрица M:\n", M)
    print("Элементы (0,1) и (2,2):", M[[0, 2], [1, 2]])


# Главная функция урока
def feature_indexing():
    indexing_1d()
    indexing_2d()
    boolean_masks()
    dataset_filtering()
    advanced_indexing()

