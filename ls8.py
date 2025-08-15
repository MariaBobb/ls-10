#Описание: Вычислить сумму всех чисел во вложенном списке любой глубины.

lst = [1, 2, [1, 2, 3], 4, [1, 2, 3, [1, 2, 3, [1, 2, 3]]]]

def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) == int:
            s += x
        else:
            s += sum_list(x)
    return s


lst = [1, 2, [1, 2, 3],  4,
       [1, 2, 3, [1, 2, 3, [1, 2, 3]]]
       ]

print(sum_list(lst))

#Описание: Исполнитель может прибавлять 1 или 3. Найдите количество способов получить 17 из 1, пройдя через 9.

def count_paths(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return count_paths(x+1, y) + count_paths(x+3, y)

    
result = count_paths(1, 9) * count_paths(9, 17)
print(f"Количество программ: {result}")

#Отфильтровать все города, названия которых начинаются на букву А
cities = 'Анапа Анадырь Москва Абакан Альметьевск Омск'
cities = cities.split()

for city in cities:
    if city[0] == 'А':
        print(city)

cities = filter(lambda x: x[0] == 'А', cities)

cities = filter(lambda x: x.startswith('А'), cities)

print(*cities)


#Отфильтровать все файлы с расширением py
#имена_файлов = 'main.py run.py main.bat app.py fastapi.py command.com'



# Проверка отсутствия русских букв
string = '1 a1 фb2 Петя ab Маша100 abc100 10'.split()

# res = map(lambda x: x.isalpha(), string)

res = filter(str.isascii, string)
res = filter (lambda x: not x.isascii(), string)
print(*res)

quad = '5 10 25 30 49 81 100'

# Проверяем, является ли число полным квадратом
def is_quad(n):
   sqtr_n = int(n ** (1/2))
   return sqtr_n ** 2 == n

# Фильтруем полные квадраты

quad = list(map(int, quad.split()))
perfect_squares = filter(is_quad, quad)
print("Полные квадраты:", *perfect_squares)  # ['25', '49', '81', '100']

# Задача 7. Посчитать площадь квартиры с помощью карты (+ reduce*)
# = комнаты [
#  {"название": "кухня", "длина": 6, "ширина": 4},
#  {"название": "комната 1", "длина": 5,5, "ширина": 4,5},
#  {"название": "комната 2", "длина": 5, "ширина": 4},
#  {"название": "комната 3", "длина": 7, "ширина": 6,3},
# ]
# '''

# print(f"Общая площадь квартиры: {total_area} кв. м") # 88,25 кв. м
square_rooms = map(lambda room: room["length"] * room["width"], rooms)
# print(*square_rooms)

total_square = reduce(lambda s, x: s + x, square_rooms)
print (total_square)

total_square = reduce(lambda acc, room: acc + room["length"] * room["width"], rooms, 0)
print (total_square)


# Задача 3.5: Обработка списка предметов
# Отфильтровать (исключить) все предметы весом менее 500

# = items_data [
#  "зонт=1000",
#  "палатка=10000", 
#  "спички=22",
#  "котелок=543"
# ]
# print(result) # зонт палатка котелок

from itertools import product, permutations

content = "🧀🍄🍖"

# Все возможные комбинации из 2 ингредиентов (порядок не важен) 
combos_2 = product(content, repeat=2)
print(*combos_2, sep="\n")
content = "🧀🍄🍖"
# Все возможные комбинации из 2 ингредиентов (порядок не важен) 
combos_2 = product(content, repeat=2)
print(*combos_2, sep="\n")
# расположить 3 ингредиента на пицце (порядок важен)
print('------')
combos_3 = permutations(content, 2)
print(*combos_3, sep="\n")

print('------')
combos_4 =  combinations(content, 2)
print(*combos_4, sep="\n")

from random import shuffle, sample
import time

suits = "♠️♥️♦️♣️" # Пики, Червы, Бубны, Трефы 
values = ('6','7','8','9','10','J','Q','K','A')

cards = list(product(suits, values))
shuffle(cards)
# извлечь 5 карт

while True:
    time.sleep(1)
    sample_cards = sample(cards, 5)
    print(*sample_cards)
    # если выпало 3 буби - победа ! 
    # стоп игра
    res = filter(lambda x: x[0] == '♦️', sample_cards)
    if len(list(res)) == 3:
        print("Победа !")
        break
    
    
    
    text = '''   
1. Последнее королевство 2015
2. Рим 2005
3. Версаль 2015
4. Тюдоры 2007
5. Террор 2018
6. Человек в высоком замке 2015
7. Белая королева 2013
8. Братья по оружию 2001
9. Медичи 2016
10. Спартак 2010
'''




# print(f"Количество строк: {line_count}")
# print(f"Количество слов: {word_count}") # не считаем цифры
# print(f"Число символов: {char_count}") # не считая пробелы

text = text.strip().splitlines()

print(*text,sep='\n')

line_count = len(text)

print(f"Количество строк: {line_count}")
# print(f"Количество слов: {word_count}") # не считаем цифры и точки # isdigit isalnum
# print(f"Число символов: {char_count}") # не считая пробелы