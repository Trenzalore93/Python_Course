# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 3
i = 0
min = k
min_index = 0
for i in range(len(list_1)):
    temp = abs(list_1[i] - k)
    if temp <= min:
        min = temp
        min_index = i
print(list_1[min_index])