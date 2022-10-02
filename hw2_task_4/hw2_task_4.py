
# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число n: '))

arr_n = []
positions = [1, 6, 8]


for i in range(-n, n+1):
    arr_n.append(i)

print(arr_n)

print(arr_n[positions[0]] * arr_n[positions[1]] * arr_n[positions[2]])