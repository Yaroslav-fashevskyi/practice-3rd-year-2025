import random


# Функція для генерації двох однорозрядних чисел (1-9)
def generate_numbers():
   a = random.randint(1, 9)
   b = random.randint(1, 9)
   return a, b


# Функція для перевірки відповіді
def check_answer(a, b, answer):
   if answer == a * b:
       print("Молодець! Дуже добре!")
       return True
   else:
       print("Невірно! Спробуйте знову ...")
       return False


# Основна програма
def main():
   while True:
       a, b = generate_numbers()
       while True:
           try:
               user_answer = int(input(f"Скільки буде {a} на {b}? "))
               if check_answer(a, b, user_answer):
                   break  # Переходимо до наступного питання
           except ValueError:
               print("Будь ласка, введіть ціле число!")


# Запуск
main()
