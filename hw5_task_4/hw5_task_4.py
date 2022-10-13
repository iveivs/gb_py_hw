# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


numb_list_1 = ['DDDDDS:WWDW DDJDJJJ WDWDWWWWWW']  # создаём список строк и записываем его в файл 1
data1 = open('file_hw5_4.txt', 'w')
data1.writelines(numb_list_1)
data1.close()

data2 = open('file_hw5_4.txt', 'r')   # распаковываем список 1, переводим его в int и создаём новый список
str_input = data2.readline()
data2.close()

# сжимаем в список

count_el = 1

res_list = []                         
for i in range(1, len(str_input)):
    curent_symb = str_input[i]
    prev_symb = str_input[i - 1]
    if curent_symb == prev_symb:
        count_el += 1
    if curent_symb != prev_symb or i == len(str_input) - 1:
        res_list.append([count_el, prev_symb])
        count_el = 1
print(f'Сжатые данные из строки в виде списка: {res_list}')
print()


# сжимаем в строку

res_str = ''                      

for i in range(1, len(str_input)):
    curent_symb = str_input[i]
    prev_symb = str_input[i - 1]
    if curent_symb == prev_symb:
        count_el += 1
    if curent_symb != prev_symb or i == len(str_input) - 1:
        res_str += f'{count_el}{prev_symb}'
        count_el = 1
print(f'Сжатые данные из строки в виде строки: {res_str}')
print()


# Востановление

out_res = ''
for i in res_list:
    out_res += i[0] * i[1]
print(f'Востановление сжатых данных: {out_res}')

 # Записываем полученный результат в файл 

data3 = open('file_hw5_4out.txt', 'w')   
data3.writelines(res_str)
data3.close()

