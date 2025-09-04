import numpy as np
import matplotlib.pyplot as plt

# Базовые статистические функции
def basic_statistics():
    data = np.array([5, 10, 15, 20, 25])
    print("\n✅ Исходный массив:", data)
    print("Сумма:", data.sum())
    print("Среднее:", data.mean())
    print("Минимум:", data.min())
    print("Максимум:", data.max())
    print("Стандартное отклонение:", data.std())


# Статистика по строкам и колонкам
def statistics_by_axis():
    M = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    print("\n✅ Матрица M:\n", M)
    print("Среднее по строкам:", M.mean(axis=1))
    print("Среднее по колонкам:", M.mean(axis=0))


# Генерация случайных данных
def random_data():
    rand_ints = np.random.randint(1, 10, size=(3, 3))
    print("\n✅ Случайные целые числа:\n", rand_ints)

    rand_floats = np.random.rand(2, 5)
    print("✅ Случайные вещественные числа:\n", rand_floats)

    normal = np.random.randn(1000)
    print("✅ Нормальное распределение (среднее ~0, σ ~1):")
    print("Среднее:", normal.mean(), "Стд. отклонение:", normal.std())


# Анализ датасета (оценки студентов)
def dataset_analysis():
    grades = np.random.randint(50, 101, 100)
    print("\n✅ Оценки студентов:", grades[:10], "...")  # показываем первые 10
    print("Средняя оценка:", grades.mean())
    print("Лучший результат:", grades.max())
    print("Худший результат:", grades.min())
    print("Сдали экзамен (>60):", (grades > 60).sum(), "из 100")

    # Визуализация распределения
    plt.hist(grades, bins=10, color="skyblue", edgecolor="black")
    plt.title("Распределение оценок студентов")
    plt.xlabel("Оценка")
    plt.ylabel("Количество студентов")
    plt.show()


# Главная функция урока
def feature_stats():
    basic_statistics()
    statistics_by_axis()
    random_data()
    dataset_analysis()

