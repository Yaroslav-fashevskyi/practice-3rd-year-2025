text = input("Введіть рядок (до n символів): ")


open_brackets = []
close_brackets = []


for i, char in enumerate(text):
   if char == '[':
       open_brackets.append(i)
   elif char == ']':
       close_brackets.append(i)


# Виведення результатів
print("Кількість відкритих дужок: ", len(open_brackets))
print("Кількість закритих дужок: ", len(close_brackets))


if open_brackets:
   print("Позиції відкритих дужок:", open_brackets)
else:
   print("Відкритих дужок немає.")


if close_brackets:
   print("Позиції закритих дужок:", close_brackets)
else:
   print("Закритих дужок немає.")


# Перевірка балансу
if len(open_brackets) != len(close_brackets):
   print("Баланс дужок порушено: кількість відкритих і закритих не збігається.")
else:
   # Перевіряємо, чи кожна [ має відповідну ] справа
   balanced = True
   for i in range(len(open_brackets)):
       if open_brackets[i] > close_brackets[i]:
           balanced = False
           break
   if balanced:
       print("Дужки збалансовані.")
   else:
       print("Дужки не збалансовані: є закриття перед відкриттям.")