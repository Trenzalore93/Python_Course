# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: 

def same_by(characteristic, objects):
    first = characteristic(objects[0])
    return all([characteristic(obj) == first for obj in objects])


values = [0, 2, 10, 6] 
if same_by(lambda x: x % 3, values):
    print("same")
else:
    print("different")