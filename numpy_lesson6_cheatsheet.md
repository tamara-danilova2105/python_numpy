
# NumPy Шпаргалка — Урок 6 (Работа с файлами и форматами)

сохранение и загрузка массивов в разных форматах.

---

## Импорт
```python
import numpy as np
```

---

## Сохранение и загрузка одного массива (.npy)

```python
arr = np.arange(10)

np.save("array.npy", arr)       # сохранить
loaded = np.load("array.npy")   # загрузить

print(loaded)
```

---

## Сохранение и загрузка нескольких массивов (.npz)

```python
a = np.arange(5)
b = np.linspace(0, 1, 5)

np.savez("arrays.npz", first=a, second=b)
data = np.load("arrays.npz")

print(data["first"])
print(data["second"])
```

---

## Сохранение и загрузка CSV

```python
arr = np.random.rand(3, 3)

np.savetxt("matrix.csv", arr, delimiter=",", fmt="%.3f")
loaded_csv = np.loadtxt("matrix.csv", delimiter=",")

print(loaded_csv)
```

---

## Прикладная задача: сохранение датасета

```python
X = np.random.rand(100, 5)        # 100 объектов × 5 признаков
y = np.random.randint(0, 2, 100)  # бинарные метки

np.savez("dataset.npz", features=X, labels=y)
data = np.load("dataset.npz")

print(data["features"][:5])  # первые 5 строк признаков
print(data["labels"][:10])   # первые 10 меток
```

---

# Главное из урока
- `np.save` / `np.load` → быстрый бинарный формат `.npy` для одного массива.
- `np.savez` / `np.load` → работа с несколькими массивами.
- `np.savetxt` / `np.loadtxt` → CSV и текстовые файлы.
- Используется для **сохранения подготовленных датасетов** и передачи между скриптами.

