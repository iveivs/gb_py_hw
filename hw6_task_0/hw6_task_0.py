# Старые задачи с приминением новых возможностей:

# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

start_arr = [1.1, 1.2, 3.49, 5, 10.01]

new_arr = filter(lambda i: i % 1 != 0, start_arr)

fract_arr = [num % 1 for num in new_arr]

a = max(fract_arr)
b = min(fract_arr)
c = round(a - b, 7)
print(c)

exit()

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# input_str = "Забвение сочетания букв абв"
# mod_inp_str = input_str.split(' ')


# new_arr = [i for i in mod_inp_str if 'абв' not in i]

# out_str = ", ".join(new_arr)
# print(f'"{out_str}"')