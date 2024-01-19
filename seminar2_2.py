# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Fn = Fn-1 + Fn-2

a = int(input('Введите натуральное число: '))
first = 0
second = 1
i = 2
if a == 0:
    print('1')
elif a == 1:
    print('2')
else:
    while second < a:
        first, second = second, first + second
        i += 1
    if second == a:
        print(i)
    else:
        print(-1)