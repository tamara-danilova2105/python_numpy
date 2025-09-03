
# 🧮 NumPy Шпаргалка — Урок 1 (База)

Этот урок покрывает основы работы с массивами и матрицами в NumPy.

---

## 📦 Импорты
```python
import numpy as np
import matplotlib.pyplot as plt
```

---

## 🔹 Создание массивов

```python
arr = np.array([1, 2, 3, 4, 5])       # массив из списка
zeros = np.zeros((3, 3))              # матрица 3x3 из нулей
ones = np.ones((2, 4))                # матрица 2x4 из единиц
arange = np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)       # равномерно 5 чисел между 0 и 1
```

---

## 🔹 Арифметика и Broadcasting

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b        # [11, 22, 33]
a * b        # [10, 40, 90]
a + 5        # [6, 7, 8] (Broadcasting)
```

---

## 🔹 Матрицы

```python
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

A + B           # поэлементное сложение
A * B           # поэлементное умножение
np.dot(A, B)    # матричное умножение (линейная алгебра)
```

---

## 🔹 Анализ случайной матрицы

```python
M = np.random.rand(10, 5)   # 10 строк × 5 колонок

M.mean(axis=0)   # среднее по колонкам
M.max(axis=1)    # максимум по строкам
M.min(axis=1)    # минимум по строкам
```

### Нормализация
```python
M_norm = (M - M.min(axis=0)) / (M.max(axis=0) - M.min(axis=0))
```

---

## 🔹 Визуализация

```python
plt.imshow(M_norm, cmap="viridis", aspect="auto")
plt.colorbar(label="Значение")
plt.title("Heatmap нормализованной матрицы")
plt.show()
```

---

## 📌 Главное из урока
- NumPy = быстрые массивы и матрицы.
- Broadcasting = операции с числами без циклов.
- Матричное умножение = ключ к ML и нейросетям.
- Нормализация = подготовка данных для моделей.
- Визуализация помогает "увидеть" данные.
