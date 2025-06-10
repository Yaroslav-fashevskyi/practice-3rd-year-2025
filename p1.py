# Введення масиву
array = list(map(float, input("Введіть дійсні числа через пробіл: ").split()))

# 1. Максимальний за модулем елемент
max_by_abs = max(array, key=abs)
print("Максимальний за модулем елемент:", max_by_abs)

# 2. Сума елементів між першим і другим додатними
positive_indices = [i for i, val in enumerate(array) if val > 0]

if len(positive_indices) < 2:
    print("У масиві менше двох додатних елементів.")
else:
    first = positive_indices[0]
    second = positive_indices[1]
    between_sum = sum(array[first+1:second])
    print("Сума між першим і другим додатними елементами:", between_sum)
