import sqlite3

def create_db():
    bd = sqlite3.connect("hw8/try_to_modul/Data_Base_Try_to_Model.db")

    cursor = bd.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS personal(
        id INTEGER PRIMARY KEY autoincrement,
        name TEXT,
        last_name TEXT,
        position TEXT,
        salary INT,
        bonus INT
    )''')

    baza = [(1,"Иван", "Иванов", "главный бухгалтер", 50000, 10000),
    (2,"Петр", "Петров", "звхоз", 23456, 4000),
    (3,"Сидор", "Сидоров", "инжинер", 43211, 5000)]

    try:
        cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', baza)
        bd.commit()
    except:
        print('Данные уже есть')

    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)





# Обзор базы

def previev_base():
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)


# Ввод данных от пользователя, для добавления нового сотрудника

def input_new_data():
    res_list = []
    colnm = 6
    i = 0
    while i < colnm:
        if i == 0:
            y = int(input("Введите id: "))
            res_list.append(y)
        if i == 1:
            y = input("Введите Имя: ")
            res_list.append(y)
        if i == 2:
            y = input("Введите Фамилию: ")
            res_list.append(y)
        if i == 3:
            y = input("Введите Должность: ")
            res_list.append(y)
        if i == 4:
            y = int(input("Введите Зарплату: "))
            res_list.append(y)
        if i == 5:
            y = int(input("Введите Премию: "))
            res_list.append(y)
        i = i + 1
    
    new_per_data = tuple(res_list)

    return new_per_data

def add_new_person():
    try:
        cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)', input_new_data())
        bd.commit()
    except:
        print('Данные не записаны')

    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)



# Удаление информации о сотруднике

def delete_record():
    inp_user = input('Введите id сотрудника для удаления информации: ')
    cursor.execute(f'DELETE FROM personal WHERE id={inp_user}')
    bd.commit()

    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)

# Поиск сотрудника

def find_record():
    inp_user = input('Введите фамилию для поиска информации о сотруднике: ')

    cursor.execute(f'SELECT * FROM personal WHERE last_name LIKE "{inp_user}";')
    one = cursor.fetchmany()
    print(one)
