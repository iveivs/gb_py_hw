from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(-2, 5))
print(f'До сортировки: {numbers}')

numbers.sort()
print(f'После сортировки: {numbers}')

numbers.sort(reverse = True)
print(f'После сортировки: {numbers}')

import random
random.shuffle(numbers)
print(f'Случайное перемешивание: {numbers}')