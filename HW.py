# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

n = int(input('Введите число: '))
res = 0
while n > 0:
    res = res + n % 10
    n = n // 10
print(res)