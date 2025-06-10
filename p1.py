full_name = input("Введіть прізвище, ім’я та по-батькові: ")


# Розділення на частини (припускаємо, що формат правильний)
parts = full_name.strip().split()
if len(parts) < 1:
   print("Некоректний ввід!")
else:
   surname = parts[0]
   surname_modified = surname.replace('а', '').replace('о', '').replace('А', '').replace('О', '')
   print("Прізвище без 'а' та 'о':", surname_modified)