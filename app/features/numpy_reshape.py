import numpy as np

# Изменение формы массива
def reshape_example():
    arr = np.arange(12)
    print("\n✅ Исходный массив:", arr)

    M = arr.reshape(3, 4)
    print("Матрица 3x4:\n", M)


# Разворачивание в одномерный массив
def flatten_example():
    M = np.arange(12).reshape(3, 4)
    print("\n✅ Матрица M:\n", M)
    print("flatten():", M.flatten())
    print("ravel():", M.ravel())


# Конкатенация массивов
def concatenate_example():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("\n✅ Конкатенация 1D массивов:", np.concatenate([a, b]))

    M1 = np.array([[1, 2],
                   [3, 4]])
    M2 = np.array([[5, 6]])
    print("✅ Конкатенация 2D по axis=0:\n", np.concatenate([M1, M2], axis=0))


# Стек массивов (vstack, hstack)
def stack_example():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("\n✅ vstack:\n", np.vstack([a, b]))
    print("✅ hstack:\n", np.hstack([a, b]))


# Разделение массивов
def split_example():
    arr = np.arange(10)
    print("\n✅ Исходный массив:", arr)

    print("split на 2 части:", np.split(arr, 2))
    print("array_split на 3 части:", np.array_split(arr, 3))


# Главная функция урока
def feature_reshape():
    reshape_example()
    flatten_example()
    concatenate_example()
    stack_example()
    split_example()

