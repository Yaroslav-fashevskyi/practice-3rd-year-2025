import math


# Початкове значення
A = [1]


# Генеруємо наступні 4 елементи (разом буде 5)
for i in range(4):
   next_A = A[i] / (1 + math.sqrt(A[i]))
   A.append(next_A)


# Обчислюємо добуток
product = 1
for a in A:
   product *= a


# Виводимо результат
print("Перші 5 елементів ряду:", A)
print("Добуток перших 5 елементів:", product)