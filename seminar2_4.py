# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# 5 -> 5 1 6 5 9

count = int(input('Введите количество арбузов: '))
fruit = []
for i in range(count):
    fruit.append(int(input("Введите вес арбуза: ")))
max_fruit = fruit[0]
min_fruit = fruit[0]
for x in fruit:
    if max_fruit < x:
        max_fruit = x
    if min_fruit > x:
        min_fruit = x
print(min_fruit, ',', max_fruit)
print(min(fruit), ',', max(fruit))