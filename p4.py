suma = 0
count = 0


print("Вводьте числа (ввід завершується після 0):")
while True:
   x = int(input("Число: "))
   if x == 0:
       break
   if 1 < x < 8:
       suma += x
       count += 1


print(f"Сума чисел в інтервалі (1, 8): {suma}")
print(f"Кількість чисел в інтервалі (1, 8): {count}")
