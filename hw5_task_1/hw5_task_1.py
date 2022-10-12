# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

input_str = "Забвение сочетания букв абв"
mod_inp_str = input_str.split(' ')

new_arr = []

for elem in mod_inp_str:
    if 'абв' not in elem:
        new_arr.append(elem)

out_str = ", ".join(new_arr)
print(f'"{out_str}"')
