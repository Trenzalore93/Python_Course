# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int(input('Введите число: '))
# f = 1
# while n > 1:
#     f *= n
#     n -= 1
# print(f)

# n = int(input('Введите число: '))
# f = 1
# i = 1
# while i <= n:
#     f *= i
#     i += 1
# print(f)

# n = int(input('Введите число: '))
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)

n = int(input('Введите число: ')) # в обратном порядке
f = 1
for i in range(n, 0, -1):
    f *= i
print(f)