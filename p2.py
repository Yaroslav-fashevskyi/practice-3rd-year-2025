import math


# Функція для обчислення r(x, y, z)
def r(x, y, z):
   return x**2 + y**2 + math.sqrt(z)


# Функція для обчислення t(x, y, z)
def t(x, y, z):
   r_value = r(x, y, z)
   return 1 - 1 / r_value


# Функція для введення аргументів
def input_args():
   x = float(input("Введіть x: "))
   y = float(input("Введіть y: "))
   z = float(input("Введіть z (z ≥ 0): "))
   if z < 0:
       raise ValueError("z має бути не менше 0 для кореня!")
   return x, y, z


# Основна функція
def main():
   x, y, z = input_args()
   r_result = r(x, y, z)
   t_result = t(x, y, z)
   print(f"\nr(x, y, z) = {r_result}")
   print(f"t(x, y, z) = {t_result}")


main()
