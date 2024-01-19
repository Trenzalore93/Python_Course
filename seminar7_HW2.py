# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# По умолчанию номер столбца и строки = 9. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.



# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows > 2:
#         for x in range(1, num_rows + 1):
#             nums = []
#             for y in range(1, num_columns + 1):
#                 num = operation(x, y)
#                 nums.append(num)
#             print(' '.join([str(x) for x in nums]))
#     else: print("ОШИБКА! Размерности таблицы должны быть больше 2!")

# print_operation_table(lambda x, y: x * y)

import os

with open('phone.txt', 'r+') as file: 
    data = {}
    for line in file:
        phone, family_name, first_name, second_name = line.split('\t')
        data[phone] = [family_name, first_name, second_name]
    print(len(data))