import json

with open("hw7_json.json", "r") as json_file:
    ivanova = json.load(json_file)

input_name = input('Введите фамилию:')

if input_name == 'Иванова':
    print(ivanova)
else:
    print('Такой фамилии нет в базе!')
