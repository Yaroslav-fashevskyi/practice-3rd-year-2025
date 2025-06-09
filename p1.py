# ВАРІАНТ 9 — НЕПАРНИЙ
# Завдання 1: Введення чисел та формування масиву згідно з умовою

def is_valid(n):
    # Умова: по модулю менше 8 і більше 3
    return 3 < abs(n) < 8

array = []
print("Введіть не більше 10 цілих чисел:")

while len(array) < 10:
    try:
        num = int(input(f"Число {len(array)+1}: "))
        if is_valid(num):
            array.append(num)
    except ValueError:
        print("Помилка: введіть ціле число.")

print("Сформований масив:", array)

# -----------------------------------------------
# Завдання 2: Для непарного варіанта — сортування за зростанням

array.sort()  # впорядковуємо масив по зростанню
print("Масив після сортування:", array)

# -----------------------------------------------
# Завдання 3: Аналіз елементів — додатні, від’ємні, середнє

positives = [x for x in array if x > 0]
negatives = [x for x in array if x < 0]

# Сума та кількість додатніх
sum_pos = sum(positives)
count_pos = len(positives)

# Добуток та кількість від’ємних
product_neg = 1
for x in negatives:
    product_neg *= x
count_neg = len(negatives)

# Середнє арифметичне
average = sum(array) / len(array) if array else 0

# Вивід результатів
print("Сума додатніх елементів:", sum_pos)
print("Кількість додатніх елементів:", count_pos)
print("Добуток від’ємних елементів:", product_neg if count_neg else "немає")
print("Кількість від’ємних елементів:", count_neg)
print("Середнє арифметичне масиву:", round(average, 2))
