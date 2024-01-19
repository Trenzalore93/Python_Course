# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# my_list = input('Введите элементы множества').split()
# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])

my_list = [int(i) for i in input('Введите элементы множества: ').split()]
k = int(input('Введите k: '))
print(my_list[-k:] + my_list[:-k])