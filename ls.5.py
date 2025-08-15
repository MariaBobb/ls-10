#text = input("Введите текст длиной минимум 5 символов: ")
#l = len(text)
#print(l)
#while len(text)<5:
#    text = input("Неверно! Введите текст длиной минимум 5 символов: ")
#print(f"Вы ввели '{text}'.Его длина {l} символов.")

#i = 0
#while True:
#    print(i)
#    i+=1
#    if i > 100:
#        break


#text = "Тестовая строка текста."
#p = "в"
#print(text.find("Тест"))
#print(text.index("е"))
#print(f"Подстрока '{p}' найдена в {text.find(p)} позиции.")

#t = "Это тестовая строка текста"
#print(t.replace("с","ф"))

#t = "Я люблю яблоки"
#print(t.replace("яблоки","апельсины"))

#t = "Я люблю яблоки, потому что яблоки вкусные!"
#s = t.replace(","," ")
#s2 = s.replace("!","")
#print(s2)

#s = "Посчитаем количество пробелов в этой строке"
#print(s.count(" "))
#s = "Посчитаем количество точек в этой строке"
#print(s.count("."))

#s = "Мои питомцы: кошка Сима, кошка Рита, кот Кекс"
#print(f"У меня есть {s.count("кошка")} кошки")

#s = "Имена сотрудников отдела Артём Иванов, Артём Филатов, Егор Нестеров, Артём Синицин"
#print(f"В нашем отделе {s.count("Артём")} Артёма ")

#t = "     Это строка с лишними пробелами.       "
#s = t.strip()  #убирает лишние пробелы
#print(t)
#print(s)

#t = "Маша и Миша"
#s = t.lower() #все маленькие
#print(t)
#print(s)
#x = t.upper() # все большие буквы
#print(x)
#z = t.capitalize() #первая буква заглавная

#t = "LADA Granta"
#print(t.startswith("LADA"))
#if t.startswith("LADA"):
#    print("Этот автомобиль марки LADA")
    
    
#t = input("Введите расстояние")
#if t.endswith("см"):
#    print("Это расстоние в сантиметрах")
#elif t.endswith("мм"):
#    print("Это расстоние в милиметрах")
#elif t.endswith("км"):
#   print("Это расстоние в километрах")
#elif t.endswith("м"):
#    print("Это расстоние в метрах")   


#print("Happy \n new \n   year!")

s = input("Введите ФИО: ")
#print(s.replace(" ","\n"))
f,i,o = s.split() #разрезает строку по пробелам
#print(f" Фамилия:  {f}")
#print(f"Имя: {i}")
#print(f"Отчество: {o}")
str = f"|{f} | {i} | {o} |"
print("-"* len(str))
print(str)
print("-"*len(str))





