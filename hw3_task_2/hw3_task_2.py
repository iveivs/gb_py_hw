# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_arr = [2, 3, 4, 5, 6]
new_arr = []

for i in range(0, len(my_arr) // 2):
    new_arr.append(my_arr[i] * my_arr[-i - 1])
if len(my_arr) % 2:
    new_arr.append(my_arr[(len(my_arr) // 2)] ** 2)
    
print(new_arr)







