
from collections import Counter

str_inp = 'дом, дом, окно, дверь, стена, стол, стул, дверь, дом, стул, стол'
new_str_inp = str_inp.split()


counter = Counter(new_str_inp)
print(counter)


# Предыдущие попытки(не довёл до конца)
# count_el = 1
# res_list = '' 

# for i in range(1, len(new_str_inp) + 1):
#     if i < len(new_str_inp):
#         curent_symb = new_str_inp[i]
#         prev_symb = new_str_inp[i - 1]
#         if curent_symb == prev_symb:
#             count_el += 1
#         if curent_symb != prev_symb or i == len(new_str_inp) - 1:
#             res_list += f'{prev_symb} {count_el}, '
#             count_el = 1
#     elif curent_symb != prev_symb:
#         res_list += f'{new_str_inp[-1]} {count_el}, '

# print(res_list)



# for i in range(1, len(new_str_inp) + 1):
#     if i < len(new_str_inp):
#         curent_symb = new_str_inp[i]
#         prev_symb = new_str_inp[i - 1]
#         if curent_symb == prev_symb:
#             count_el += 1
#         if curent_symb != prev_symb or i == len(new_str_inp) - 1:
#             res_list.append([prev_symb, count_el])
#             count_el = 1
#     elif curent_symb != prev_symb:
#         res_list.append([new_str_inp[-1], count_el])

# print(res_list)