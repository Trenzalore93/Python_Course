# def calk1(a,b):
# #     return a+b

# # calk1 = lambda a,b: a + b

# def calk2(a,b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)


def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
