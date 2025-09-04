import numpy as np

# Сохранение и загрузка одного массива (.npy)
def save_and_load_npy():
    arr = np.arange(10)
    np.save("array.npy", arr)       # сохранить
    loaded = np.load("array.npy")   # загрузить

    print("\n✅ Исходный массив:", arr)
    print("Загруженный массив:", loaded)


# Сохранение и загрузка нескольких массивов (.npz)
def save_and_load_npz():
    a = np.arange(5)
    b = np.linspace(0, 1, 5)

    np.savez("arrays.npz", first=a, second=b)
    data = np.load("arrays.npz")

    print("\n✅ Сохранены массивы .npz")
    print("Первый массив:", data["first"])
    print("Второй массив:", data["second"])


# Сохранение и загрузка CSV
def save_and_load_csv():
    arr = np.random.rand(3, 3)

    np.savetxt("matrix.csv", arr, delimiter=",", fmt="%.3f")
    loaded_csv = np.loadtxt("matrix.csv", delimiter=",")

    print("\n✅ Исходная матрица:\n", arr)
    print("Загруженная из CSV:\n", loaded_csv)


# Прикладная задача: сохранение датасета
def dataset_io():
    X = np.random.rand(100, 5)        # 100 объектов × 5 признаков
    y = np.random.randint(0, 2, 100)  # бинарные метки

    np.savez("dataset.npz", features=X, labels=y)
    data = np.load("dataset.npz")

    print("\n✅ Датасет сохранён в dataset.npz")
    print("Признаки (первые 5 строк):\n", data["features"][:5])
    print("Метки (первые 10):", data["labels"][:10])


# Главная функция урока
def feature_io():
    save_and_load_npy()
    save_and_load_npz()
    save_and_load_csv()
    dataset_io()

