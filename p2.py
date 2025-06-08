def process(suma=0, count=0):
   x = int(input("Введіть число (0 — завершити): "))
   if x == 0:
       print(f"Сума чисел в інтервалі (1, 8): {suma}")
       print(f"Кількість чисел в інтервалі (1, 8): {count}")
       return
   if 1 < x < 8:
       suma += x
       count += 1
   process(suma, count)


process()
