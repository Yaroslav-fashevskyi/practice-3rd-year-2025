import random


# Розмір квадратної матриці
n = 4  # Можна змінити на будь-яке число


# Створення випадкової квадратної матриці n x n
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]


print("Початкова матриця:")
for row in matrix:
   print(row)


# Заміна останнього рядка і першого стовпця
for i in range(n):
   # Міняємо місцями matrix[i][0] (1-й стовпець) з matrix[n-1][i] (останній рядок)
   matrix[i][0], matrix[n - 1][i] = matrix[n - 1][i], matrix[i][0]


print("\nМатриця після заміни останнього рядка і першого стовпця:")
for row in matrix:
   print(row)