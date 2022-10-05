# 3.Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

start_arr = [1.1, 1.2, 3.49, 5, 10.01]

new_arr = []

for i in start_arr:
    if i % 1 != 0:
        new_arr.append(i)


fract_arr = [num % 1 for num in new_arr]

a = max(fract_arr)
b = min(fract_arr)
c = round(a - b, 7)
print(c)