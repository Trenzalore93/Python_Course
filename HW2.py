# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

n = int(input('Введите количество журавликов: '))
a = int(n / 6)
b = int(4 * a)
print(f"{a} {b} {a}")