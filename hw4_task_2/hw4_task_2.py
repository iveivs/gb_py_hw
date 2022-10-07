# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Задайте натуральное число: '))
simp_num_arr = []
divsn = 2
while(divsn <= n):
    if (n % divsn) == 0:
        simp_num_arr.append(divsn)
        n = n / divsn
    else:
        divsn += 1

print(simp_num_arr)
