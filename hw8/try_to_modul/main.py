import model
from model import create_db, previev_base, add_new_person, delete_record, find_record



def input_choice():
    create_db()
    while True:
        user_choise = input('1 - посмотреть базу:, 2 - добавить запись:, 3 - удалить запись:, 4 - найти по Ф.И.О:, q - выход:')
        if user_choise == "1":
            previev_base()
        elif user_choise == "2":
            add_new_person()
        elif user_choise == "3":
            delete_record()
        elif user_choise == "4":
            find_record()
        elif user_choise == "q":
            print('Выход')
            break
        elif user_choise != "1" and user_choise != "2" and user_choise != "3" and user_choise != "4" and user_choise != "q":
            print('Такой команды в программе не существует')
            break


input_choice()