# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.


import os
import shutil

def data_input(data):
    while True:
        user_input = input('Введите номер телефона: ')
        if not user_input or not user_input.isdigit():
            return data
        if user_input in data:
            print('Такой номер уже есть')
        else:
            temp = input('Введите Фамилию, Имя, Отчество: ').split()
            if len(temp) != 3:
                print('Ошибка')
            else:
                data[user_input] = temp
                with open('phone.txt', 'a') as f: 
                    print(f"{user_input}\t{temp[0]}\t{temp[1]}\t{temp[2]}", file = f)
                return data

def show_data(data):
    for key, value in data.items():
        print(key, *value)
      
def copy_data(data):
    line_number = input('Введите номер строки\n')
    lines = tuple(data)
    if line_number in range(len(lines)+1):
        with open('new.txt', 'a') as destination: 
                destination.writelines(lines[line_number-1])
    else:
        print('Такой строки не существует')
        return

def search_data(data):
    user_input = input("Поиск 1: номер телефона или 2: иное")
    if user_input not in {'1', '2'}:
        return
    if user_input == '1':
        phone = input("введите номер телефона: ")
        print(data.get(phone, 'Нет номера'))
        return
    other = input("Имя или Фамилия или Отчество")
    if ' ' in other or not other:
        print('Ошибка')
        return
    for key, values in data.items():
        for value in values:
            if other in value:
                print(key, *values)
                break

def main():
    if os.path.exists('phone.txt'):
        with open('phone.txt', 'r+') as file: 
            data = {}
            for line in file:
                phone, family_name, first_name, second_name = line.split('\t')
                data[phone] = [family_name, first_name, second_name]
    else:
        with open('phone.txt', 'a') as file:
            data = {}
    
    print('Добро пожаловать в телефонный справочник')
    while True:
        while True:
            user_input = input('''1 - ввести новые данные \n2 - посмотреть данные \n3 - поиск данных\n4 - копирование данных справочника\n5 - выход \n''')
            if user_input not in {'1', '2', '3', '4', '5'}:
                print('Неверный ввод')
            else:
                break
        if user_input == '1':
            data = data_input(data)
        if user_input == '2':
            show_data(data)
        if user_input == '3':
            search_data(data)
        if user_input == '4':
            copy_data(data)
        else:
            print('До свидания!')
            break 

if __name__ == '__main__':
    main()



    





