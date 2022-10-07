# 3.Задайте последовательность чисел. 
#   Напишите программу, которая выведет список неповторяющихся э
#   лементов исходной последовательности.

numbers = [1, 9, 7, 3, 3, 4, 5, 4]

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    uniq_numb = set(numbers)

    for number in uniq_numb:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))

