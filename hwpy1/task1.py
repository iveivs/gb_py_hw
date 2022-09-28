input_day_num = int(input("Укажите номер дня недели: "))

def kind_of_days(number):
    week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if number < 1 or number > 7:
            print('Вы указали некорректное значение')
    elif number < 6:
        print(f' {week[number - 1]} - будний день, не выходной!')
    else:
        print(f' {week[number - 1]} - выходной день!')

kind_of_days(input_day_num)