# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

#  Пример:
#     Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717

n = int(input('Введите число: '))
out_arr = []
j = 0
for i in range(1, n+1):
    form = (1 + 1/i)**i
    out_arr.append(form)
    summa = sum(out_arr)

print(out_arr)
print(summa)